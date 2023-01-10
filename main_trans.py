import pkg_resources
import sys, os
import requests
import pyperclip
import keyboard
from time import sleep
from time import time
import tkinter as tk
import tkinter.font as tkFont

while True:

    query = pyperclip.paste()
    oldQuery = pyperclip.paste()
    while query == oldQuery:
        try:
            query = pyperclip.paste()
        except:
            continue
        if keyboard.is_pressed('ctrl+q'):
            os.kill(launcher_trans.exe)
        sleep(0.1)

    url = 'https://translate.googleapis.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': 'auto',
        'tl': 'en',
        'dt': 't',
        'q': query
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for i in range(len(data[0])):
            output = data[0][i][0].replace('\n', ' ')
            print(output)
    else:
        output = 'An error occurred:', response.status_code
        print(output)


    # Create the main window
    window = tk.Tk()

    # Make the window appear at the front of all the other windows
    window.attributes("-topmost", True)

    # window background colour
    window.configure(bg="#23272a", bd=10, relief=tk.RIDGE)

    # Remove the title bar
    window.overrideredirect(True)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    (lw, lh) = ((tkFont.Font(family="Rockwell", size=36)).measure(output),(tkFont.Font(family="Rockwell", size=36)).metrics("linespace"))
    print(lh)

    # Create a label with the text
    label = tk.Label(window, text = output, font = ("Rockwell", 36), fg="#ffffff", bg = "#23272a", wraplength=screen_width)
    label.pack()
    label.update()
    lines = int(label.winfo_height() / lh)
    print(lines)
    
    # Set the window position
    window.geometry("{}x{}+{}+{}".format(int(screen_width), int(((screen_height/11) * lines) - 8*lines + 15), int(0), int(screen_height/2)))

    # Schedule the window to be destroyed after 2000 milliseconds (2 seconds)
    window.after(1500 + (len(output)*38), lambda: window.destroy())

    # Run the main loop
    window.mainloop()
