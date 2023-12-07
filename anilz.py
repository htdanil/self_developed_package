#Quickly get data from sqlite database give sql and path function
def sqlite_get(sql,db_path):
	import pandas as pd
	import sqlite3
	conn_sqlite = sqlite3.connect(db_path)
	dd = pd.read_sql(sql,conn_sqlite)
	conn_sqlite.close()
	return dd

#Quickly get and store data into sqlite database from excel
def excel_to_sqlite(excel_path,sheet_name,db_path):
	import pandas as pd
	import sqlite3
	df = pd.read_excel(excel_path, sheet_name=sheet_name)
	conn_sqlite = sqlite3.connect(db_path)
	df.to_sql(sheet_name,conn_sqlite,if_exists = 'replace')
	conn_sqlite.close()

#Quickly get and store data into sqlite database from csv
def csv_to_sqlite(csv_path,db_path,table_name):
	import pandas as pd
	import sqlite3
	df = pd.read_csv(csv_path)
	conn_sqlite = sqlite3.connect(db_path)
	df.to_sql(table_name,conn_sqlite,if_exists = 'replace')
	conn_sqlite.close()

def print_sourcecode(obj):
	import inspect
	print(inspect.getsource(obj))

def eng2uni(txt):
	return txt.replace("1","१").replace("2","२")\
	.replace("3","३").replace("4","४")\
	.replace("5","५").replace("6","६")\
	.replace("7","७").replace("8","८")\
	.replace("9","९").replace("0","०")

def uni2eng(txt):
	return txt.replace("१","1").replace("२","2")\
	.replace("३","3").replace("४","4")\
	.replace("५","5").replace("६","6")\
	.replace("७","7").replace("८","8")\
	.replace("९","9").replace("०","0")

def search_object(obj, search_keyword):
	lst = [x for x in dir(obj)]
	return [x for x in lst if search_keyword.lower() in x.lower() ]

#========================================================================================

ndate_calendar = [[2000, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2001, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2002, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2003, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2004, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2005, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2006, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2007, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2008, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
 [2009, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2010, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2011, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2012, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
 [2013, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2014, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2015, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2016, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
 [2017, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2018, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2019, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2020, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2021, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2022, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
 [2023, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2024, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2025, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2026, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2027, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2028, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2029, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
 [2030, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2031, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2032, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2033, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2034, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2035, 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
 [2036, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2037, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2038, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2039, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
 [2040, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2041, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2042, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2043, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
 [2044, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2045, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2046, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2047, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2048, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2049, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
 [2050, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2051, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2052, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2053, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
 [2054, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2055, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2056, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
 [2057, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2058, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2059, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2060, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2061, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2062, 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31],
 [2063, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2064, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2065, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2066, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
 [2067, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2068, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2069, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2070, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
 [2071, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2072, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
 [2073, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
 [2074, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2075, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2076, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
 [2077, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
 [2078, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
 [2079, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
 [2080, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
 [2081, 31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30],
 [2082, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
 [2083, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
 [2084, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
 [2085, 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30],
 [2086, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
 [2087, 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30],
 [2088, 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30],
 [2089, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
 [2090, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
 [2091, 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30]]



def ad2bs(ad_date):
    from datetime import datetime, timedelta, date
    starting_range_ad = datetime.strptime('04/14/1943', '%m/%d/%Y')
    
    ad_date = str(ad_date).replace("-"," ").replace("."," ").replace("/"," ").replace(","," ").split(" ") #replacing possible separator charector to space for split
    ad_year = int(ad_date[0])
    ad_month = int(ad_date[1])
    ad_day = int(ad_date[2])
    
    
    gap = date(ad_year, ad_month, ad_day) - starting_range_ad.date()
    if gap.days < 0:
        return 'Provided AD out of range!!!!'
    
    days_count = 0
    break_the_loop = False
    for x in ndate_calendar:
        for i in range(1,13):
            days_count = days_count + x[i]
            if days_count > gap.days:
                break_the_loop = True
                break
        if break_the_loop:
            year = str(x[0])
            if i < 10:
                month = '0' + str(i)
            else:
                month = str(i)

            day = (x[i] - (days_count - gap.days) + 1)
            if day < 10:
                day = '0' + str(day)
            else:
                day = str(day)      

            return year+'-'+month+'-'+day
            break
    
    return 'Provided AD out of range!!!!'
            
def bs2ad(bs_date):
    from datetime import datetime, timedelta, date
    starting_range_ad = datetime.strptime('04/14/1943', '%m/%d/%Y')
    
    bs_date = bs_date.replace(".","-").replace("/","-").replace(",","-").split('-')
    bs_year = int(bs_date[0])
    bs_month = int(bs_date[1])
    bs_day = int(bs_date[2])
    
    if bs_year < ndate_calendar[0][0]:
        return 'Provided BS out of range!!!!'
    
    days_count = 0
    break_the_loop =False
    for x in ndate_calendar:
        for i in range(1,13):
            if x[0] == bs_year and i == bs_month:
                days_count = days_count + bs_day
                break_the_loop = True
                break
            days_count = days_count + x[i]
    
        if break_the_loop:
            return (starting_range_ad + timedelta(days=days_count-1)).date()
    return 'Provided BS out of range!!!!'
        
def bs2ad_str(bs_date):
    return str(bs2ad(bs_date))







###########################################################################################################################################################################
# webVar class for storing data/variables to the web where [ROOT\Anil\Python App\MISC_PYTHON_GIT\noSQLite api (simplified with commit functionality)] is hosted.
###########################################################################################################################################################################
import requests
import json
import base64

class webVar:
  def __init__(self, web_url, var_collection):
    self.web_url = web_url
    self.var_collection = var_collection

  def push(self, var_name, data):
    data_encoded = base64.b64encode(data.encode('utf-8')).decode()
    x = {"db" : "webVar.db",
         "actions" : [
            {
                "type" : "insert",
                "collection" : self.var_collection,
                "records" : [
                    {"var_name" : var_name,
                     "data" : data_encoded }
                ]
            }
         ]
    }

    self.drop(var_name)

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/records", data=json.dumps(x), headers=headers).json()
    self.response = response

    if response['status'] == 'FAILED':
      print(response)

  def drop(self, var_name):
    x = {"db" : "webVar.db",
         "actions" : [
            {
                "type" : "delete",
                "collection" : self.var_collection,
                "condition" : f"var_name == '{var_name}'"
            }
         ]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/records", data=json.dumps(x), headers=headers).json()
    self.response = response

  def get(self, var_name):
    x = {"db" : "webVar.db",
     "collection" : self.var_collection,
     "condition" : f"var_name == '{var_name}'"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/select", data=json.dumps(x), headers=headers).json()
    self.response = response

    if response['status'] == 'FAILED' or len(response['data']) ==0 :
      print("No variable found : " + str(response))
    else:
      return base64.b64decode(response['data'][0]['data']).decode('utf-8')

  def get_all(self):
    x = {"db" : "webVar.db",
      "collection" : self.var_collection
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/get", data=json.dumps(x), headers=headers).json()
    self.response = response

    if response['status'] == 'FAILED' or len(response['data']) ==0 :
      print("No variable found : " + str(response))
    else:
      return response['data']
  
  def list_var_collection(self):
    x = {"db" : "webVar.db"}

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/collection_list", data=json.dumps(x), headers=headers).json()
    self.response = response
    print(response)

  
  def drop_var_collection(self, var_collection):
    x = {"db" : "webVar.db",
      "collection" : var_collection
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(self.web_url+"/api/drop", data=json.dumps(x), headers=headers).json()
    self.response = response
    print(response)