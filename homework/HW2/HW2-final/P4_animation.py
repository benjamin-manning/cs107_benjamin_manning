import numpy
import matplotlib.pyplot as plt
import datetime
from math import pi, sin, cos

### Closure defined up here
fig = plt.figure(figsize=(6,6))
def hour_closure(r):
    def hour_hand(hour_theta):
        nonlocal r
        hour_theta = pi*hour_theta/180
        return .5*r*cos(hour_theta), .5*r*sin(hour_theta)
    return hour_hand

def minute_closure(r):
    def minute_hand(minute_theta):
        nonlocal r
        minute_theta = pi*minute_theta/180
        return r*cos(minute_theta), r*sin(minute_theta)
    return minute_hand

def second_closure(r):
    def second_hand(second_theta):
        nonlocal r
        second_theta = pi*second_theta/180
        return 1.3*r*cos(second_theta), 1.3*r*sin(second_theta)
    return second_hand

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

x=True
count = 60
def show_clock(animation_length):
    while animation_length > 0:
        r = 10
        hour_hand = hour_closure(r)
        minute_hand = minute_closure(r)
        second_hand = second_closure(r)

        hour, minute, second = get_time()
        hour_theta, minute_theta, second_theta = get_theta(hour, minute, second)

        plt.axis([-r*1.4, r*1.4, -r*1.4, r*1.4])
        plt.axis('off')

        x_hour, y_hour = hour_hand(hour_theta)
        x_minute, y_minute = minute_hand(minute_theta)
        x_second, y_second = second_hand(second_theta)

        plt.plot([0, x_hour], [0, y_hour], 'r', linewidth=6)
        plt.plot([0, x_minute], [0, y_minute], 'b', linewidth=6)
        plt.plot([0, x_second], [0, y_second], 'g')
        fig.canvas.draw()
        plt.pause(.01)
        plt.cla()
        animation_length -=1
show_clock(500)

