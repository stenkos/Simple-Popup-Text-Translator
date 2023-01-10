# Simple Popup Text Translator
## *IMPORTANT - After days of suffering I have retired this repo. Enjoy this buggy mess.*
## Overview
This program translates text that you copy into your clipboard, into the English language. When text is translated, it is displayed via a simplistic and modern GUI. The colour scheme of the GUI is based on the Discord colour scheme and uses Discord Black (#23272A) for the background and Discord White (#FFFFFF) for the text.

The translation is performed by the Google Translate API `translate_a` endpoint.

## Installation
The program's executable will be available shortly. Instead, to run it in a Python interpreter, download the files or clone the repository using:

`${GIT REPO}`

Make sure the required packages are installed by running:

`pip install -r requirements.txt`

The main translation program is in `main-trans.py`, but I am trying to integrate it into a system tray program in `launcher-trans.py`.

## Extra Info
### The translated text
I have not yet added functionality for language translation other than to English. To add your own language, enter the `main.py` file and in the Google Translate `params`, replace the target language (`tl`) with your preferred language in ISO shortform.
### The console
The console may print random samples during the runtime of the code. This is (in order):

 - The translated text
 - 54
 - The number of lines
 
This is a byproduct of my debugging, which I will fix in the next iteration of my program.
### To-do list
- [ ] Fix the tray icon
- [ ] Add a language selection tool
- [ ] Properly compile the program
- [ ] Fix the jankiness of the window
- [ ] Push window onto the middle every time
