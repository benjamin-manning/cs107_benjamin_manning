from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

city_weather_prediction={}

for city in city_weather:
    weather = Markov(day_zero_weather=city_weather[city])
    weather.load_data(file_path='./weather.csv')
    prediction = weather._simulate_weather_for_day(7,trials=100)
    city_weather_prediction[city]= prediction

for city in city_weather_prediction:
    print(city,':', city_weather_prediction[city])

print('\nMost likely weather in seven days\n---------------------------------')
for city in city_weather_prediction:
    weather_guess= max(city_weather_prediction[city], key=city_weather_prediction[city].get)
    print(city, ':', weather_guess)