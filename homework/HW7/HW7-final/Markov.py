import numpy as np
from collections import Counter

class Markov:
    def __init__(self,day_zero_weather = None,total_days=10): # You will need to modify this header line later in Part C
        self.data = np.array([])
        self.weather_dict={'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
        if day_zero_weather != None:
             assert day_zero_weather in self.weather_dict.keys(), Exception(f'Invalid weather type {day_zero_weather}')

        self.data = np.array([])
        self.current_weather=day_zero_weather
        self.total_days=total_days

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        current_day_weather=current_day_weather.lower()
        next_day_weather=next_day_weather.lower()

        assert current_day_weather in self.weather_dict.keys(), Exception(f'Invalid weather type {current_day_weather}')
        assert next_day_weather in self.weather_dict.keys(), Exception(f'Invalid weather type {next_day_weather}')
        
        return self.data[self.weather_dict[current_day_weather],self.weather_dict[next_day_weather]]
    
    def __iter__(self):
        return MarkovIterator(self)

    def get_weather_for_day(self, day):
        self.total_days = day      
        self.day_number = 0
        for day in self:
            next_day = day
        return next_day

    def _simulate_weather_for_day(self,first_day,trials=100):
        assert first_day >= 0, ValueError(f'Argument is less than 0.')
        if first_day is 0:
            return self.current_weather
        else:
            list_of_trials=[]
            counter = 0
            while counter < trials:
               list_of_trials.append(self.get_weather_for_day(first_day))
               counter +=1
            return dict(Counter(list_of_trials))
      

class MarkovIterator:
    def __init__(self, tracker):
        
        self.iterator = tracker
        self.current_weather= self.iterator.current_weather
        self.total_days = self.iterator.total_days
        self.weather_list = list(self.iterator.weather_dict.keys())
        self.day_number=0

    def __iter__(self):
        return self

    def __next__(self):
        self.day = self.current_weather
        if self.day_number > self.total_days:
            raise StopIteration()
        self.day_number += 1
        probabilities = [self.iterator.get_prob(self.day, weather) for weather in self.weather_list]
        next_day = np.random.choice(self.weather_list, 1, p=probabilities)
        self.day = next_day[0]
        return self.day
