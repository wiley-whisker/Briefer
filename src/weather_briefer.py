"""
An app that displays the weather forcast for the day.

author: Wiley Matthews.
"""

import tkinter as tk
import requests
import io

from PIL import Image, ImageTk
from urllib.request import urlopen
from bs4 import BeautifulSoup

AWC_BASE_URL = 'https://www.aviationweather.gov'
AWC_PROG_PAGE = 'https://www.aviationweather.gov/progchart/sfc'
DARKSKY_HOURLY_CALL = 'https://api.darksky.net/forecast/b3f609149b1cdc25c712bba1f8c20430/43.15,-77.68?exclude=minutely,daily,alerts,flags'


def get_prog():
    response = requests.get(AWC_PROG_PAGE)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    prog_img = soup.find('img', {"id": "image"})
    prog_url = AWC_BASE_URL + prog_img['src']
    return urlopen(prog_url).read()


def get_weather():
    pass


def resize_img(img, w, h):
    return Image.open(io.BytesIO(img)).resize((w, h), Image.ANTIALIAS)


def main():
    root = tk.Tk()
    root.title("Briefer")

    # Size screen
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%sx%s' % (width, height))
    weather_frame = tk.Frame(root, background='#8f8f8f')

    weather_frame.pack(side='right', fill='both', expand=True)

    # Get and display prog chart
    prog_img = resize_img(get_prog(), width, height)
    prog_chart = ImageTk.PhotoImage(prog_img)
    canvas = tk.Canvas(root, bg='white', width=width//2, height=height)
    canvas.pack(anchor='w')
    canvas.create_image(width//2, 0, image=prog_chart, anchor='ne')

    #
    tk.Label(weather_frame, text="Today's Weather", font=("Helvetica", 40)).pack()


    root.mainloop()

    # Get images

if __name__ == '__main__':
    main()



