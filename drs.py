try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import imutils
from functools import partial
import threading
import time
import os
from ttkthemes import ThemedTk
from tkinter.ttk import *

stream = cv2.VideoCapture("clip/clip.mp4")
def play(speed):
    try:
        video_frame = stream.get(cv2.CAP_PROP_POS_FRAMES)
        stream.set(cv2.CAP_PROP_POS_FRAMES, video_frame+speed)
        grabbed, frame = stream.read()
        frame  = imutils.resize(frame, width=WIDTH, height=HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=NW)

    except:
        print("No more Frames Available")


def pending(decision):

    frame = cv2.cvtColor(cv2.imread("images/sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=NW)

    time.sleep(1.5)

    frame = cv2.cvtColor(cv2.imread("images/pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=NW)

    time.sleep(2)
    time.sleep(1)

    if decision == "out":
        decisionImg = "images/out.png"
    else:
        decisionImg = "images/notout.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    #print("Out!")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    #print("Not Out")

def reset():
    exit()
    



WIDTH = 720
HEIGHT = 480

window = ThemedTk(theme="")
window.title("DRS System by RjRahul")
window.geometry("720x595")
window.resizable(0, 0)
window.iconbitmap("images/icon.ico")

cv_img = cv2.cvtColor(cv2.imread("images/bg.jpg"), cv2.COLOR_BGR2RGB)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
img_on_canvas = canvas.create_image(0, 0, anchor=NW, image=photo)
button = Button(window, text="<<Previous (fast)", width=50, command=partial(play, -25))
button.pack()

button = Button(window, text="<<Previous (slow)", width=50, command=partial(play, -2))
button.pack()

button = Button(window, text="Next (slow)>>", width=50, command=partial(play, 2))
button.pack()

button = Button(window, text="Next(fast)>>", width=50, command=partial(play, 25))
button.pack()

#button = Button(window, text="Give Out", width=50, bg="red", command=out)
#button.pack()

#button = Button(window, text="Give Not Out", width=50, bg="green", command=not_out)
#button.pack()

btn_imgo = cv2.cvtColor(cv2.imread("images/o.png"), cv2.COLOR_BGR2RGB)
btn_out = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(btn_imgo))
button = Button(window, text="not out", image=btn_out, command=out)
#button.pack(side=TOP, anchor=NW)
button.place(x=10, y=490)


btn_imgno = cv2.cvtColor(cv2.imread("images/no.png"), cv2.COLOR_BGR2RGB)
btn_not = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(btn_imgno))
button = Button(window, text="not out", image=btn_not, command=not_out)
#button.pack(side=TOP, anchor=NW)
button.place(x=600, y=490)

reset_btn = Button(window, text="Reset", command=reset).place(x=14, y=16)

window.mainloop()

