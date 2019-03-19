#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in Space: ', result['number'])
people = result['people']
for i in people:
  print(i['name'], ' in ', i['craft'])

screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape('station.gif')

iss = turtle.Turtle()
iss.shape('station.gif')
iss.setheading(90)
iss.penup()

while(True):
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
  
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('Latitude: ', lat)
    print('Longitude: ', lon)
    
    # map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
    screen.bgpic('worldmap.gif')


    iss.goto(float(lon), float(lat))
    iss.pendown()

    time.sleep(5)
turtle.done()
