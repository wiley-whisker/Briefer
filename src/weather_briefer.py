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
    def __init__(self, w_data):
        tk.Frame.__init__(self)
        self.w_data = w_data
        self.pack(side='left')
        self.make_content()

    def make_content(self):
        self.photo = get_image()
        tk.Label(self, text=self.w_data['summary'] + " - " + self.w_data['time'], font=("Helvetica", 10)).pack(
            side='top')  # .grid(row=pos[0], column=pos[1])
        self.cv = tk.Canvas(self, bg='#d1d1d1', width=self.photo.width(), height=self.photo.height())
        self.cv.pack(side='top')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')
        tk.Label(self, text=self.w_data['date'] + " - " + self.w_data['time'], font=("Helvetica", 10)).pack(side='top')



def get_image():
    sym = r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\cloudy.png'  # static path for now.
    sym_image = Image.open(sym)
    return ImageTk.PhotoImage(sym_image)


def resize_img(img, w, h):
    return img.resize((w, h), Image.ANTIALIAS)


def main():
    root = tk.Tk()
    root.title("Briefer")

    # Size screen
    width = root.winfo_screenwidth()
    height = round(root.winfo_screenheight()*0.9)
    root.geometry('%sx%s' % (width, height))

    print(width, height)

    num_rows = 6
    for i in range(num_rows):
        root.grid_rowconfigure(i, minsize=height // num_rows)

    num_columns = 12
    for i in range(num_columns):
        root.grid_columnconfigure(i, minsize=width // num_columns)

    # prog_frame = tk.Frame(root, bg='purple', width=width//2, height=height)
    # weather_frame = tk.Frame(root, bg='yellow', height=height, width=width//2)

    # forecast_summary = tk.Frame(forecast_frame, bg='pink')
    # forecast_upper = tk.Frame(forecast_frame, bg='orange')
    # # forecast_lower = tk.Frame(forecast_frame, bg='purple')
    #
    #
    # forecast_summary.grid(row=0)
    # forecast_upper.grid(row=1)
    # forecast_lower.grid(row=2)

    # Get and display prog chart
    # prog_img = resize_img(weather.get_prog(), width, height)
    prog_chart = ImageTk.PhotoImage(Image.open(r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\prog_test.gif'))
    canvas = tk.Canvas(root, bg='white', width=width//2, height=height)
    canvas.grid(row=0, column=0, rowspan=num_rows-2, columnspan=num_columns//2)
    canvas.create_image(width//2, 0, image=prog_chart, anchor='ne')
    #
    # # Get and display weather data
    tk.Label(root, text="Today's Weather", font=("Helvetica", 20)).grid(row=0, column=7, columnspan=3)

    current, outlook, forecast = weather.get_forecast()  # GET WEATHER DATA

    sym = r'C:\Users\Wiley\Documents\python_projects\Briefer\assets\cloudy.png'  # static path for now.
    sym_image = resize_img(Image.open(sym), 100, 100)
    photo = ImageTk.PhotoImage(sym_image)

    current_frame = tk.Frame(root)
    tk.Label(current_frame, text=current['summary'], font=("Helvetica", 10)).pack()
    cv1 = tk.Canvas(current_frame, bg='#d1d1d1', width=photo.width(), height=photo.height())
    cv1.pack()
    cv1.create_image(0, 0, image=photo, anchor='nw')
    tk.Label(current_frame, text=current['date'] + " - " + current['time'], font=("Helvetica", 10)).pack()
    tk.Label(current_frame, text=str(current['precipProbability']) + " - " + str(current['temperature']), font=("Helvetica", 10)).pack()
    current_frame.grid(row=1, column=8)
    #
    # tk.Label(forecast_summary, text="Summary", font=("Helvetica", 20)).pack(side='bottom')
    #
    # for i in range(5):
    #     tk.Label(forecast_upper, text="SummaryU", font=("Helvetica", 10)).grid(row=0, column=i)
    #     tk.Label(forecast_upper, text="SummaryL", font=("Helvetica", 10)).grid(row=1, column=i)
    for i in range(2):
        for j in range(num_columns//2, num_columns):
            for_frame = tk.Frame(root)
            tk.Label(for_frame, text=current['summary'], font=("Helvetica", 10)).pack()
            cv = tk.Canvas(for_frame, bg='#d1d1d1', width=photo.width(), height=photo.height())
            cv.pack()
            cv.create_image(0, 0, image=photo, anchor='nw')
            tk.Label(for_frame, text=current['date'] + " - " + current['time'], font=("Helvetica", 10)).pack()
            tk.Label(for_frame, text=str(current['precipProbability']) + " - " + str(current['temperature']),
                     font=("Helvetica", 10)).pack()
            for_frame.grid(row=i+2, column=j)

    # for i in range(num_rows):
    #     for j in range(num_columns//2, num_columns):
    #         tk.Label(root, text="grid({},{})".format(i, j)).grid(row=i, column=j)


    # stuff = [[],[]]
    # for i in range(3):
    #     stuff [0].append(WeatherBox(forecast_upper, (0, 0), current).make_content())
    # for i in range(3):
    #     stuff[1].append(WeatherBox(forecast_lower, (0, 0), current).make_content())

    # COLOR_BOIS = ('orange', 'green', 'purple', 'pink', 'blue', 'red')

    root.mainloop()


if __name__ == '__main__':
    main()



