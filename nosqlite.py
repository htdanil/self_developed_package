class noSQLite:
    def __init__(self, db_path):
        import sqlite3
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.collection_lst()
    
    def get_1D_dict(self, d): #converts multilevel dictionary to one level dictionary
        dd = {}
        for r in d.keys():
            if 'dict' in str(d[r].__class__):
                ddd = self.get_1D_dict(d[r])
                for rr in ddd.keys():
                    dd[r+'.'+rr] = ddd[rr]
            else:
                dd[r] = d[r]
        return dd
    
    def collection_lst(self):
        import pandas as pd
        self.collection_list = list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", self.conn)['name'])
    
    def insert_many_records(self,collection, records): #insert many records
        if 'str' in str(type(records)):
            import json
            records = json.loads(records)
            
        for r in records:
            self.insert_record(collection,r)
    
    def insert_record(self, collection, records): #insert single record
        import pandas as pd

        if 'str' in str(type(records)):
            import json
            records = json.loads(records)

        self.collection_lst()
        records = self.get_1D_dict(records)
        tbl_fields = ''
        for r in list(records.keys()):
            tbl_fields += f"'{r}' text, "
            
        if collection not in self.collection_list:
            self.conn.execute("CREATE TABLE '{0}' ({1})".format(collection, tbl_fields[:-2]))
            self.collection_lst()
        
        tbl_fields = tbl_fields[:-2].replace('text','')
        columns = list(pd.read_sql_query("select * from '{}'".format(collection), self.conn).columns)
        
        for r in list(records.keys()):
            if r not in columns:
                self.conn.execute("ALTER TABLE '{0}' ADD COLUMN '{1}' text".format(collection, r))
                #self.conn.commit()
        
        self.conn.execute("INSERT INTO '{0}' ({1}) values ({2})".format(collection, tbl_fields, str(list(records.values()))[1:-1]))
        #self.conn.commit()
        self.collection_lst()
    
    def retrieve_df(self, sql):
        import pandas as pd
        df = pd.read_sql_query(sql, self.conn, chunksize = 5000)
        chunk_list = []
        try:
            for data_chunk in df: 
                chunk_list.append(data_chunk)
            return pd.concat(chunk_list)
        except:
            return pd.DataFrame({})
    
    def get_all(self, collection): #get all data in json format
        sql = f"select rowid, * from `{collection}`"
        return self.df_to_json(self.retrieve_df(sql))
    
    def get_all_df(self, collection): #get all data in dataframe format
        sql = f"select rowid, * from `{collection}`"
        return self.retrieve_df(sql)
        
    def df_to_json(self, df):
        exec('self.records =' + str(df.to_json(orient='records').replace('null','"null"')))

        key_value_pair_list = []

        for r in self.records:
            key_lst = list(r.keys())
            for rr in key_lst:
                if r[rr] == 'null':
                    del r[rr]

            key_list = list(r.keys())
            final_key_value_pair = {}
            for k in key_list:
                lst = k.split('.')
                if len(lst) > 1:
                    x = ''
                    for i in range(len(lst)):
                        try:
                            exec('final_key_value_pair' + x + f"['{lst[i]}']")
                        except:
                            exec('final_key_value_pair' + x + f"['{lst[i]}']"+'={}')

                        if i == len(lst) - 1:
                            exec('final_key_value_pair' + x + f"['{lst[i]}']"+f'=r[k]')

                        x += f"['{lst[i]}']"
                else:
                    final_key_value_pair[k] = r[k]
            key_value_pair_list.append(final_key_value_pair)
        
        return key_value_pair_list
    
    def select(self,collection,condition):
        sql = f"select rowid, * from `{collection}` where {condition}"
        return self.df_to_json(self.retrieve_df(sql))
    
    def select_df(self,collection,condition):
        sql = f"select rowid, * from `{collection}` where {condition}"
        return self.retrieve_df(sql)
    
    def commit(self):
        self.conn.commit()
        self.collection_lst()

    def rollback(self):
        self.conn.rollback()

    def drop_collection(self,collection):
        self.conn.execute(f'DROP TABLE `{collection}`')
        #self.conn.commit()
        self.collection_lst()
    
    def delete_records(self,collection,condition):
        sql = f"DELETE from `{collection}` where {condition}"
        self.conn.execute(sql)
        #self.conn.commit()
        
    def update_records(self,collection,set_values,condition):
        import pandas as pd
        columns = list(pd.read_sql_query("select * from '{}'".format(collection), self.conn).columns)
               
        set_columns = []
        for s in set_values.split('and'):
            set_columns.append(s.split('=')[0].strip().replace('`','').replace("'",'').replace('"',''))
        
        for r in set_columns:
            if r not in columns:
                self.conn.execute("ALTER TABLE '{0}' ADD COLUMN '{1}' text".format(collection, r))
        
        sql = f"UPDATE `{collection}` SET {set_values} where {condition}"

        self.conn.execute(sql)
        #self.conn.commit()
        
    def remove_null_columns(self): #null columns cannot be dropped due to limited functionality of sqlite
        import pandas as pd
        
        null_columns = {}
        for c in self.collection_list:
            null_columns[c]=[]
            columns = list(pd.read_sql_query(f'select * from `{c}` where 1=2', self.conn).columns)
            for cc in columns:
                count = pd.read_sql_query(f'select count(*) from `{c}` where `{cc}` is not null', self.conn).iat[0,0]
                if count == 0:
                    null_columns[c].append(cc)
        
        return {'null_columns_to_be_deleted':null_columns}
         
    def close(self):
        self.conn.close()