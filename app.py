import requests as r
import pprint
import json
from flask import Flask
from flask import request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)



@app.route('/')
def weatherdata():
    api_key = "FLASK_API_KEY"
    response = r.get("https://api.forecast.io/forecast/%s/%s,%s"%(api_key,16.5189,80.3613))
    content = response.content
    data  = json.loads(content)
    lat = data['latitude']
    timezone = data['timezone']
    currently = data['currently'] 
    summary =  data['currently']['summary'] 
    temperature = data['currently']['temperature']
    cel= (temperature-32.0)/(9.0 / 5.0);
    cel = round(cel,2)
    prec = data['currently']['precipIntensity']
    hum = data['currently']['humidity']
    wind = data['currently']['windSpeed']
    return render_template('sample.html', lat = lat, summary=summary,timezone = timezone,hum = hum,wind = wind,cel = cel,prec = prec)


if __name__ == '__main__':
    app.run(debug=True)
