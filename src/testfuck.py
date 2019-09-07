import tkinter as tk
from time import sleep

root = tk.Tk()
H = tk.Frame(root)
h = tk.Label(H, text="Fuck").pack()
H.pack()
root.update()
sleep(2)
H.pack_forget()
root.update()
sleep(3)

