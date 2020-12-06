"""
Morgan Christensen

Image viewer with tkinter
"""
from tkinter import *
from PIL import ImageTk,Image


# commands for cycling through pictures
def forward(img_num):
    global img_label
    global b_forward
    global b_back

    img_label.grid_forget()
    img_label = Label(image=img_list[img_num - 1])
    bf = Button(window, text="Next", command=lambda: forward(img_num + 1))
    bb = Button(window, text="Back", command=lambda: backward(img_num - 1))
    if img_num == len(img_list):
        bf.configure(state=DISABLED)
    img_label.grid(row=0, column=0, columnspan=3)
    status.configure(text="Image {} of {}".format(img_num, len(img_list)))
    bb.grid(row=1, column=0)
    bf.grid(row=1, column=2)


def backward(img_num):
    global img_label
    global b_forward
    global b_back

    img_label.grid_forget()
    img_label = Label(image=img_list[img_num - 1])
    bf = Button(window, text="Next", command=lambda: forward(img_num + 1))
    bb = Button(window, text="Back", command=lambda: backward(img_num - 1))
    if img_num == 1:
        bb.configure(state=DISABLED)
    img_label.grid(row=0, column=0, columnspan=3)
    status.configure(text="Image {} of {}".format(img_num, len(img_list)))
    bb.grid(row=1, column=0)
    bf.grid(row=1, column=2)

window = Tk()
window.title("Image viewer")

# Call for images from folder and make them an object
img_1 = ImageTk.PhotoImage(Image.open("highlights/DSC_0037.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("highlights/DSC_0005.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("highlights/DSC_0168.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("highlights/DSC_0234.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("highlights/DSC_0011.jpg"))
img_6 = ImageTk.PhotoImage(Image.open("highlights/DSC_0021.jpg"))

# list to hold the images to cycle through
img_list = [img_1, img_2, img_3, img_4, img_5, img_6]
total_img = len(img_list)
# status bar
status = Label(window, text="Image {} of {}".format(1, total_img), bd=5, relief=SUNKEN, anchor=E)
# label that holds the image
img_label = Label(image=img_1)
img_label.grid(row=0, column=0, columnspan=3)

bb = Button(window, text="Back", command=lambda: backward, state=DISABLED)
be = Button(window, text="Exit", command=window.quit)
bf = Button(window, text="Next", command=lambda: forward(2))

bb.grid(row=1, column=0)
be.grid(row=1, column=1)
bf.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
window.mainloop()