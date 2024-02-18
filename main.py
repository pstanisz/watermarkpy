# Copyright (c) 2024, CodeVision Piotr Staniszewski

from tkinter import Tk, filedialog, Label, Button
import cv2

window = Tk()
window.title(string="Watermark image")
window.minsize(width=800, height=600)


def browse_wmark():
    wmark_file = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=[("All", "*.*")])
    wmark = cv2.imread(wmark_file)
    cv2.imshow("mark", wmark)


def browse_image():
    img_file = filedialog.askopenfilename(initialdir="/", title="Select a File")
    img = cv2.imread(img_file)
    cv2.imshow("image", img)


wmark_label = Label(window, text="Open watermark file", width=100, height=4)
wmark_label.pack()

wmark_button = Button(window, text="Open watermark file", command=browse_wmark)
wmark_button.pack()

img_label = Label(window, text="Open image file", width=100, height=4)
img_label.pack()

img_button = Button(window, text="Open image file", command=browse_image)
img_button.pack()

window.mainloop()
