import os
import webbrowser
import datetime

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_browser():
    webbrowser.open("https://www.google.com")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")