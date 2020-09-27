import numpy
import matplotlib.pyplot as plt
import datetime
from math import pi, sin, cos

### Closure defined up here
fig = plt.figure(figsize=(6,6))

# Defining hour Closure
def hour_closure(r):
    def hour_hand(hour_theta):
        nonlocal r
        hour_theta = pi*hour_theta/180
        return .5*r*cos(hour_theta), .5*r*sin(hour_theta)
    return hour_hand

# Defining Minute Closure
def minute_closure(r):
    def minute_hand(minute_theta):
        nonlocal r
        minute_theta = pi*minute_theta/180
        return r*cos(minute_theta), r*sin(minute_theta)
    return minute_hand

#defining Second closure
def second_closure(r):
    def second_hand(second_theta):
        nonlocal r
        second_theta = pi*second_theta/180
        return 1.3*r*cos(second_theta), 1.3*r*sin(second_theta)
    return second_hand

#creating a time function
def get_time():
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second
    return hour, minute, second

hour, minute, second = get_time()

# Calculate theta in degrees for each hand

def get_theta(hour, minute, second):
    if hour > 12:
        hour = hour - 12
    hour_theta = 90-(30*hour)-(minute/2)
    minute_theta = 90-6*minute
    second_theta = 90 - 6*second
    return hour_theta, minute_theta, second_theta

hour_theta, minute_theta, second_theta = get_theta(hour, minute, second)

# Specify the length of hour, minute and second hands
r = 10
hour_hand = hour_closure(r)
minute_hand = minute_closure(r)
second_hand = second_closure(r)

# hour_hand = name_of_closure(length_of_hour_hand)

x_hour, y_hour = hour_hand(hour_theta)
x_minute, y_minute = minute_hand(minute_theta)
x_second, y_second = second_hand(second_theta)

#plotting the clock
plt.axis([-r*1.4, r*1.4, -r*1.4, r*1.4])
plt.axis('off')
plt.plot([0, x_hour], [0, y_hour], 'r', linewidth=6)
plt.plot([0, x_minute], [0, y_minute], 'b', linewidth=6)
plt.plot([0, x_second], [0, y_second], 'g')
plt.show()
plt.pause(1)
plt.cla()
exit