import tkinter as tk
from tkinter import filedialog
from organizer import organize_files

def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def run_organizer():

    path = folder_path.get()

    if path:
        organize_files(path)
        status.config(text="Files Organized Successfully!")

window = tk.Tk()
window.title("File Organizer PRO")
window.geometry("400x250")

# Background color
window.configure(bg="#2c3e50")

title = tk.Label(
    window,
    text="File Organizer PRO",
    font=("Arial", 16),
    bg="#2c3e50",
    fg="white"
)
title.pack(pady=15)

folder_path = tk.StringVar()

select_btn = tk.Button(
    window,
    text="Select Folder",
    command=select_folder,
    bg="#3498db",
    fg="white",
    width=20
)
select_btn.pack(pady=5)

path_label = tk.Label(
    window,
    textvariable=folder_path,
    bg="#2c3e50",
    fg="white"
)
path_label.pack()

organize_btn = tk.Button(
    window,
    text="Organize Files",
    command=run_organizer,
    bg="#27ae60",
    fg="white",
    width=20
)
organize_btn.pack(pady=10)

status = tk.Label(
    window,
    text="",
    bg="#2c3e50",
    fg="yellow"
)
status.pack()

window.mainloop()