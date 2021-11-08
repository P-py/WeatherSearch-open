from flask import Flask, render_template, request, flash
from flask.wrappers import Response
import requests
import json

app = Flask(__name__)

with open('./data/secret_key.0') as file:
    app.secret_key = file.read()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        
        with open('./data/key.0') as f:
            key = f.read()


        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={key}&lang=pt_br&units=metric')

        if weather_url.status_code == 404:
            flash("Couldn't find weather informations for that city. The city or country name may be wrong.", category='error')
            return render_template('index.html')

        else:
            data = weather_url.json()

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            weather = data['weather'][0]['main']
            icon_id = data['weather'][0]['icon']

            icon_url = f'http://openweathermap.org/img/wn/{icon_id}@2x.png'

            return render_template('result.html', temp=temperature, humidity=humidity, wind_speed=wind_speed, city=city, weather=weather, icon=icon_url)

    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')