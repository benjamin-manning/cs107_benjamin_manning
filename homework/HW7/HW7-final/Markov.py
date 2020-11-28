import numpy as np

class Markov:
    def __init__(self): # You will need to modify this header line later in Part C
        self.data = np.array([])
        self.weather_list = {'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        self.today = current_day_weather
        #test to see if the weather is valid
        assert current_day_weather in self.weather_list.keys(), Exception(f'Invalid weather type {current_day_weather}')
        assert next_day_weather in self.weather_list.keys(), Exception(f'Invalid weather type {next_day_weather}')
        #index into the data
        self.today_index = self.weather_list[current_day_weather]
        self.tomorrow_index = self.weather_list[next_day_weather]
        #Return the probability
        return self.data[self.today_index][self.tomorrow_index]

    def __iter__(self):
        return MarkovIterator(self.today,self.data)

class MarkovIterator:
    def __init__(self, weather_type, data):
        self.weather_type = weather_type
        self.data = data
        self.weather_list = {'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
        self.today = self.weather_list[weather_type]

    def __next__(self):
        tomorrow = np.random.choice(6, 1, replace=False, p=self.data[self.today])
        print(tomorrow)
        #return tomorrow
        

    def __iter__(self):
        return self



