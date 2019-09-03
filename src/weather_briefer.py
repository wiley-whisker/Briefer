"""
An app that displays the weather forecast for the day.

author: Wiley Matthews.
date: 9/2/2019
"""

# Standard libraries.
import tkinter as tk
import io

# External libraries.
from PIL import Image, ImageTk

# Local libraries.
from src import weather


def resize_img(img, w, h):
    return Image.open(io.BytesIO(img)).resize((w, h), Image.ANTIALIAS)


def main():
    root = tk.Tk()
    root.title("Briefer")

    # Size screen
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%sx%s' % (width, height))
    weather_frame = tk.Frame(root)

    weather_frame.pack(side='right', fill='both', expand=True)

    # Get and display prog chart
    prog_img = resize_img(weather.get_prog(), width, height)
    prog_chart = ImageTk.PhotoImage(prog_img)
    canvas = tk.Canvas(root, bg='white', width=width//2, height=height)
    canvas.pack(anchor='w')
    canvas.create_image(width//2, 0, image=prog_chart, anchor='ne')

    # Get and display weather data
    tk.Label(weather_frame, text="Today's Weather", font=("Helvetica", 40)).pack()
    current, outlook, forecast = weather.get_forecast()
    tk.Label(weather_frame, text=current['summary'], font=("Helvetica", 20)).pack()
    sym = r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\cloudy.png'  # static path for now.
    sym_image = Image.open(sym)
    photo = ImageTk.PhotoImage(sym_image)
    cv = tk.Canvas(weather_frame, bg='#d1d1d1', width=photo.width(), height=photo.height())
    cv.pack()
    cv.create_image(0, 0, image=photo, anchor='nw')
    tk.Label(weather_frame, text=current['date'] + " - " + current['time'], font=("Helvetica", 20)).pack()

    root.mainloop()

if __name__ == '__main__':
    main()



