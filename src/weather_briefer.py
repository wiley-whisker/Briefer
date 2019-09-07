"""
An app that displays the weather forecast for the day.

author: Wiley Matthews.
date: 9/2/2019
"""

# Standard libraries.
import tkinter as tk
import io
import os

# External libraries.
from PIL import Image, ImageTk

# Local libraries.
from src import weather

FONT_SIZE = 8
PHOTOS = []  # Probably the wrong way to do this, but tk needs me to keep references to the images.


def get_image(icon):
    image_dir = __file__ + '/../../assets/{}.png'.format(icon)
    sym_image = Image.open(image_dir)
    return sym_image


def resize_img(img, w, h):
    return img.resize((w, h), Image.ANTIALIAS)


def main():
    root = tk.Tk()
    root.title("Briefer")

    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()  # <-- move focus to this widget
    root.bind("<Escape>", lambda e: e.widget.quit())

    # Size screen
    width = root.winfo_screenwidth()
    height = round(root.winfo_screenheight()*1)

    print(width, height)

    num_rows = 6
    for i in range(num_rows):
        root.grid_rowconfigure(i, minsize=height // num_rows)

    num_columns = 12
    for i in range(num_columns):
        root.grid_columnconfigure(i, minsize=width // num_columns)

    # Get and display prog chart
    prog_chart = ImageTk.PhotoImage(Image.open(io.BytesIO(weather.get_prog())))
    canvas = tk.Canvas(root, bg='white', width=width//2, height=height)
    canvas.grid(row=0, column=0, rowspan=num_rows-2, columnspan=num_columns//2)
    canvas.create_image(width//2, 0, image=prog_chart, anchor='ne')

    # Get and display weather data
    tk.Label(root, text="Today's Weather", font=("Helvetica", 20)).grid(row=0, column=7, columnspan=3)

    current, outlook, forecast = weather.get_forecast()  # GET WEATHER DATA

    curr_image = resize_img(get_image(current['icon']), 100, 100)
    curr_photo = ImageTk.PhotoImage(curr_image)

    current_frame = tk.Frame(root)
    tk.Label(current_frame, text=current['summary'], font=("Helvetica", FONT_SIZE)).pack()
    cv1 = tk.Canvas(current_frame, bg='#d1d1d1', width=curr_photo.width(), height=curr_photo.height())
    cv1.pack()
    cv1.create_image(0, 0, image=curr_photo, anchor='nw')
    tk.Label(current_frame, text=current['date'] + " - " + current['time'], font=("Helvetica", FONT_SIZE)).pack()
    tk.Label(current_frame, text=str(current['precipProbability']) + " - " + str(current['temperature']), font=("Helvetica", FONT_SIZE)).pack()
    current_frame.grid(row=1, column=8)

    for_itr = 0
    for i in range(2):
        for j in range(num_columns//2, num_columns-1):
            hour_data = forecast[for_itr]
            for_itr += 1
            for_frame = tk.Frame(root)
            for_image = resize_img(get_image(hour_data['icon']), 100, 100)
            for_photo = ImageTk.PhotoImage(for_image)
            PHOTOS.append(for_photo)
            tk.Label(for_frame, text=hour_data['summary'], font=("Helvetica", FONT_SIZE)).pack()
            cv = tk.Canvas(for_frame, bg='#d1d1d1', width=for_photo.width(), height=for_photo.height())
            cv.pack()
            cv.create_image(0, 0, image=for_photo, anchor='nw')
            tk.Label(for_frame, text=hour_data['date'] + " - " + hour_data['time'], font=("Helvetica", FONT_SIZE)).pack()
            tk.Label(for_frame, text=str(hour_data['precipProbability']) + " - " + str(hour_data['temperature']),
                     font=("Helvetica", FONT_SIZE)).pack()
            for_frame.grid(row=i+2, column=j)

    root.mainloop()


if __name__ == '__main__':
    main()



