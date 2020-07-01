#!/usr/bin/env python

__author__ = 'sohailadev'

import pip._vendor.requests
import time
import turtle


def print_data_of_astronauts(url):
    """This function will print astronauts full names,
       the spacecraft they are currently on board,
       sand the total number of astronauts in space with given url
    """
    json_data = pip._vendor.requests.get(url).json()
    json_status = json_data['message']
    if json_status == 'success':
        number_of_people = json_data['number']
        names_of_people = []
        names_of_craft = []
        for each in json_data['people']:
            names_of_people.append(each['name'])
            names_of_craft.append(each['craft'])
        print(20*"**")
        print("Numbers of  Astronauts")
        print(20*"**")
        print(number_of_people)
        print(20*"**")
        print("Full names of Astronauts")
        print(20*"**")
        for each in names_of_people:
            print(each)
        print(20*"**")
        print("Crafts of Astronauts")
        print(20*"**")
        for each in names_of_craft:
            print(each)


def iss_loc(url):
    json_data = pip._vendor.requests.get(url).json()
    json_status = json_data['message']
    if json_status == 'success':
        return json_data['iss_position']


def indi_cordi(url):
    json_data = pip._vendor.requests.get(url).json()
    json_status = json_data['message']
    if json_status == 'success':
        return json_data["request"]


def show_ISS(dict_cor, dict_indi):
    lat = dict_cor['latitude']
    long = dict_cor['longitude']
    lat_indi = float(dict_indi['latitude'])
    lon_indi = float(dict_indi['longitude'])
    indi_time = time.ctime(dict_indi['datetime'])
    t = turtle.Turtle()
    t2 = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.addshape('iss.gif')
    screen.bgpic('map.gif')
    t.shape("iss.gif")
    t.setpos(float(long), float(lat))
    t2.goto(lon_indi, lat_indi)
    t2.dot(8, "yellow")
    t2.color('yellow')
    t2.write(indi_time)

    while True:
        time.sleep(2)
        print("downloading cordinatess......")
        iss_cord = iss_loc("http://api.open-notify.org/iss-now.json")
        t.setpos(float(iss_cord['longitude']), float(iss_cord['latitude']))
    turtle.mainloop()


def main():
    url_of_astronauts = "http://api.open-notify.org/astros.json"
    url_of_loc = "http://api.open-notify.org/iss-now.json"
    url_indi = f"http://api.open-notify.org/iss-pass.json?lat=39.7683333&lon=-86.1580556"
    print_data_of_astronauts(url_of_astronauts)
    iss_loc(url_of_loc)
    show_ISS(iss_loc(url_of_loc), indi_cordi(url_indi))


if __name__ == '__main__':
    main()
