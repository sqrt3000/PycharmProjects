from tkinter import *
import tkinter
from PIL import ImageTk, Image



# def foo():
#     image = ImageTk.PhotoImage(Image.open("ball.png"))


image = Image.open("screenshot_from_Chrome.png")
def mic():
    global image
    modal = Tk()
    modal.geometry('1000x1000')
    canvas = Canvas(modal, width=999, height=999)
    canvas.pack()
    pilImage = Image.open("screenshot_from_Chrome.png")
    img = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(400, 400, image=img)

    # label = Label(image=img)
    # label.image = img
    # label.pack()




root = Tk()
# Button that lets the user blur the image
btn_blur=tkinter.Button(root, text="Blur", width=50, command=mic)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)


root.mainloop()
