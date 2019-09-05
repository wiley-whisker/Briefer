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


class WeatherBox(tk.Frame):
    def __init__(self, parent, pos, w_data):
        tk.Frame.__init__(self)
        self.w_data = w_data
        self.pack(side='left')

    def make_content(self):
        self.photo = get_image()
        tk.Label(self, text=self.w_data['summary'] + " - " + self.w_data['time'], font=("Helvetica", 10)).pack(
            side='top')  # .grid(row=pos[0], column=pos[1])
        self.cv = tk.Canvas(self, bg='#d1d1d1', width=self.photo.width(), height=self.photo.height())
        self.cv.pack(side='top')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')
        tk.Label(self, text=self.w_data['date'] + " - " + self.w_data['time'], font=("Helvetica", 10)).pack(side='top')
        return self



def get_image():
    sym = r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\cloudy.png'  # static path for now.
    sym_image = Image.open(sym)
    return ImageTk.PhotoImage(sym_image)


def resize_img(img, w, h):
    return Image.open(io.BytesIO(img)).resize((w, h), Image.ANTIALIAS)


def main():
    root = tk.Tk()
    root.title("Briefer")

    # Size screen
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%sx%s' % (width, height))
    weather_frame = tk.Frame(root, bg='yellow')
    current_frame = tk.Frame(weather_frame, bg='blue')
    forecast_frame = tk.Frame(weather_frame, bg='green')
    forecast_summary = tk.Frame(forecast_frame, bg='pink')
    forecast_upper = tk.Frame(forecast_frame, bg='orange')
    forecast_lower = tk.Frame(forecast_frame, bg='purple')

    weather_frame.pack(side='right', fill='both', expand=True)
    current_frame.pack(side='top', fill='both', expand=False)
    forecast_frame.pack(side='bottom', fill='both', expand=True)

    forecast_summary.pack(side='top', fill='both', expand=True)
    forecast_upper.pack(side='top', fill='both', expand=True)
    forecast_lower.pack(side='top', fill='both', expand=True)

    # Get and display prog chart
    prog_img = resize_img(weather.get_prog(), width, height)
    prog_chart = ImageTk.PhotoImage(prog_img)
    canvas = tk.Canvas(root, bg='white', width=width//2, height=height)
    canvas.pack(anchor='w')
    canvas.create_image(width//2, 0, image=prog_chart, anchor='ne')

    # Get and display weather data
    tk.Label(current_frame, text="Today's Weather", font=("Helvetica", 40)).pack()
    current, outlook, forecast = weather.get_forecast()
    tk.Label(current_frame, text=current['summary'], font=("Helvetica", 20)).pack()
    sym = r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\cloudy.png'  # static path for now.
    sym_image = Image.open(sym)
    photo = ImageTk.PhotoImage(sym_image)
    cv = tk.Canvas(current_frame, bg='#d1d1d1', width=photo.width(), height=photo.height())
    cv.pack()
    cv.create_image(0, 0, image=photo, anchor='nw')
    tk.Label(current_frame, text=current['date'] + " - " + current['time'], font=("Helvetica", 20)).pack()

    tk.Label(forecast_summary, text="Summary", font=("Helvetica", 20)).pack(side='bottom')
    stuff = [[],[]]
    for i in range(3):
        stuff [0].append(WeatherBox(forecast_upper, (0, 0), current).make_content())
    for i in range(3):
        stuff[1].append(WeatherBox(forecast_lower, (0, 0), current).make_content())

    # COLOR_BOIS = ('orange', 'green', 'purple', 'pink', 'blue', 'red')

    root.mainloop()

if __name__ == '__main__':
    main()



