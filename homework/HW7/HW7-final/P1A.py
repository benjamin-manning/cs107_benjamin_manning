from Markov import Markov
import numpy as np

weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
print(weather_today.get_prob('cloudy', 'windy'))

print(weather_today.__iter__())