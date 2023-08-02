import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import datetime
import time
import pyttsx3
import pywhatkit
import pyautogui
import cv2
import boto3

def option_1():
    os.system("notepad")
    print("Done")

def option_2():
    os.system("chrome")
    print("Done")

def option_3():
    song=input("Enter song name:")
#     song = text.replace('song', '')
    pywhatkit.playonyt(song)

def option_4():
    count=int(input("How many instance you want to launch:"))
    myec2=boto3.client('ec2')
    myec2.run_instances(
        ImageId='ami-0ded8326293d3201b',
        InstanceType='t2.micro',
        MaxCount=count,
        MinCount=1
)

def option_5():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    engine = pyttsx3.init()
    engine.say('Current time is ' + current_time)
    engine.runAndWait()

def option_6():
    os.system("start microsoft.windows.camera:")

def option_7():
    os.system("shutdown -s")

def option_8():
    os.system("spotify")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('ya habibi', interval=0.1)
    for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
        time.sleep(2)
        pyautogui.press(key)

def option_9():
    engine = pyttsx3.init()
    engine.say("Tell me phone No")
    engine.runAndWait()
    number = input("Number please:")
    engine.say("Write your Message here:")
    engine.runAndWait()
    message = input("Message:")
    pywhatkit.sendwhatmsg_instantly(number, message)
    engine.say("Done")
    engine.runAndWait()

def option_10():
    folder_name = input("Enter folder name: ")
    os.mkdir(folder_name)

def option_11():
    folder_name = input("Enter folder name to remove: ")
    os.rmdir(folder_name)

def option_12():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    while True:
        status, photo = cap.read()
        cv2.imshow("Hi", photo)
        if cv2.waitKey(4) == 13:
            break
    cv2.destroyAllWindows()

def option_13():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    while True:
        status, photo = cap.read()
        my_grey_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Hi", my_grey_photo)
        if cv2.waitKey(4) == 13:
            break
    cv2.destroyAllWindows()

def option_14():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    cv2.imshow("Capture", photo)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    

def option_15():
    root.destroy()
    

# Create the tkinter GUI
root = tk.Tk()
root.title("Menu-Driven App")


def create_option_button(text, command):
    button_width = 20  # Set the desired width for the buttons
    button_height = 1  # Set the desired height for the buttons
    pady = 5
    button = tk.Button(root, text=text, font=("Helvetica", 12), command=command, bg="white", width=button_width, height=button_height)
    button.pack(pady=pady)

# Create buttons for each option
create_option_button("Open Notepad", option_1)
create_option_button("Open Chrome", option_2)
create_option_button("Open YouTube", option_3)
create_option_button("Launch EC2 Instance", option_4)
create_option_button("Time now", option_5)
create_option_button("Open Camera", option_6)
create_option_button("Shutdown", option_7)
create_option_button("Open Spotify", option_8)
create_option_button("WhatsApp", option_9)
create_option_button("Make Folder", option_10)
create_option_button("Remove Folder", option_11)
create_option_button("Colorful Video", option_12)
create_option_button("Grey Video", option_13)
create_option_button("Click Image", option_14)
create_option_button("Exit", option_15)



# Add buttons for the rest of the options...

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Set the background color to black
root.configure(bg="light blue")

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Exit", command=root.quit)

# Center the window on the screen
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

root.mainloop()
    