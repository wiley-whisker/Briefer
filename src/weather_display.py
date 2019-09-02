"""
A script that tests openweatherapi and displays the weather status in a tkinter window.

author: Wiley Matthews
"""

import requests
import tkinter as tk
from urllib.request import urlopen

api_key = '286145f3e532733b94b26fa96949232d'
darkSky_key = 'b3f609149b1cdc25c712bba1f8c20430'


def init_display():
    root.title("Display local weather")
    w = 520
    h = 320
    x = 80
    y = 100
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    tk.Label(root, text="City Name:").grid(row=0, column=0)
    tk.Button(root, text='Get Weather Data', command=get_weather).grid(row=0,
                                                                       column=2,
                                                                       sticky=tk.W,
                                                                       pady=4)


def get_weather():
    query = e1.get()
    api_call = 'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}, us'.format(api_key, query)
    api_res = requests.get(api_call)
    result = api_res.json()
    sym = result['weather'][0]['icon']
    image_url = 'http://openweathermap.org/img/wn/{}@2x.png'.format(sym)
    sym_image = urlopen(image_url).read()
    photo = tk.PhotoImage(data=sym_image)
    cv = tk.Canvas(bg='#8a8a8a', width=photo.width(), height=photo.height())
    cv.grid(row=0, column=3)
    cv.create_image(0, 0, image=photo, anchor='nw')
    cvs.append(photo)


root = tk.Tk()
init_display()
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
cvs = []
tk.mainloop()