import requests as r
import pprint
import json
api_key = "660aa041d1aa157e5f78ac527cd1921a"

def weatherdata(api_key,lat,log):
    response = r.get("https://api.forecast.io/forecast/%s/%s,%s"%(api_key,lat,log))
    content = response.content
    data  = json.loads(content)
    print data['latitude']
    currently = data['currently']
    for i in currently:
        print "%s-%s"%(i,currently[i])
    print data['currently']['dewPoint']
    print data['currently']['temperature']
   




weatherdata(api_key,16.5189,80.3613)