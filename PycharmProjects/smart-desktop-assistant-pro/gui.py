import tkinter as tk
from commands import open_calculator, open_notepad, open_browser, get_time

def show_time():
    time = get_time()
    label.config(text="Current Time: " + time)

def start_gui():
    global label

    window = tk.Tk()
    window.title("Smart Desktop Assistant PRO")
    window.geometry("400x300")

    title = tk.Label(window, text="Smart Desktop Assistant", font=("Arial",16))
    title.pack(pady=20)

    btn1 = tk.Button(window, text="Open Calculator", command=open_calculator, bg="lightblue", width=20)
    btn1.pack(pady=5)

    btn2 = tk.Button(window, text="Open Notepad", command=open_notepad, bg="lightgreen", width=20)
    btn2.pack(pady=5)

    btn3 = tk.Button(window, text="Open Browser", command=open_browser, bg="lightyellow", width=20)
    btn3.pack(pady=5)

    btn4 = tk.Button(window, text="Show Time", command=show_time, bg="orange", width=20)
    btn4.pack(pady=5)

    label = tk.Label(window,text="")
    label.pack(pady=10)

    window.mainloop()