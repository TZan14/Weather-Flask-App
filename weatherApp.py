from requests import get
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)  # Parent directory

# Get the data and render


@app.route('/', methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            # Get the city place
            city_input = request.form.get("city")

        # Load the weather api
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
                city_input + "&appid=a58926ec75f4a5be56140bd1abd56b11&units=metric"

            data = get(api).json()  # Get the api in json format

        # Get Current weather data
            current_temp = round(data['main']['temp'], 2)  # 2 decimal places
            feel_temp = round(data['main']['feels_like'], 2)
            max_temp = round(data['main']['temp_max'], 2)
            min_temp = round(data['main']['temp_min'], 2)
            wind = round(data['wind']['speed'], 2)
            humidity = data['main']['humidity']

        # Modify the data with units to represent in web
            city = city_input
            current_temp = str(current_temp) + ' °C'
            feel_temp = str(feel_temp) + ' °C'
            max_temp = str(max_temp) + ' °C'
            min_temp = str(min_temp) + ' °C'
            wind = str(wind) + ' m/s'
            humidity = str(humidity) + '%'

        # Names
            n_city = "Place"
            n_ctemp = "Current Temperature"
            n_ftemp = "Feels Like"
            n_max = "Maximum Temperature"
            n_min = "Minimum Temperature"
            n_wind = "Wind Speed"
            n_humi = "Humidity "
            credit = "Created by Min Thet Zan on 14th of August 2022. Powered by Open Weather API"
        # Load the data to render
            return render_template('index.html', place=city, current_temp=current_temp,
                                   feel_temp=feel_temp, max_temp=max_temp,
                                   min_temp=min_temp, wind=wind, humidity=humidity,
                                   n_city=n_city, n_ctemp=n_ctemp, n_ftemp=n_ftemp,
                                   n_max=n_max, n_min=n_min,
                                   n_wind=n_wind, n_humi=n_humi, credit=credit)
        else:
            return render_template('index.html')

    except:
        return "<h1 style = 'text-align: center;'>Something went wrong with input! The city you might not exist or spelling mistake. Check again.</h1>"


if __name__ == '__main__':
    app.run('192.168.1.8', 8080, debug=False)
