import json 
import requests



res = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)
#----------------------------------------------
url = body[38]['legislatures'][1]['popolo_url']
res2 = requests.get(url)
body2 = json.loads(res2.content)
#-----------------------------------------
name = body2['persons'][0]['given_name']
print(f'Hello My Name is {name} and I am a Senator')