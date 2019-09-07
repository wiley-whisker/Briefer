import tkinter as tk

root = tk.Tk()

x = tk.Frame(root, bg='red', width=100, height=100)
x.grid_propagate(0)
tk.Label(x, text="fuck").grid()
y = tk.Frame(root, bg='blue')
z = tk.Frame(root, bg='yellow')

x.grid(row=0, rowspan=2)
y.grid(row=0, column=1)
z.grid(row=1, column=1)

root.mainloop()
