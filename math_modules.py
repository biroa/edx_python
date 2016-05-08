from math import *

def calculate(x):
    return sin(x)-cos(x)+sin(x)*cos(x)

def calculate2(x):
    return abs(x**3)+cos(sqrt(3*x))

def distance_between_two_points(pa,pb):
    pa_x = pa[0]
    pa_y = pa[1]
    pa_z = pa[2]

    pb_x = pb[0]
    pb_y = pb[1]
    pb_z = pb[2]

    distance = sqrt(((pb_x-pa_x)**2)+((pb_y-pa_y)**2)+((pb_z-pa_z)**2))
    return distance
    
x =  int(input('give me a number:'))
print('result:',distance_between_two_points(x))

    
