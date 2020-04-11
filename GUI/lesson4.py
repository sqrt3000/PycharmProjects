from tkinter import *

root = Tk()
root.geometry('600x400+400+200')


l = Label(root, text="Тескт в строке 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5", bg="red", font=("Comic Sans MS", 10, "bold"), justify=LEFT, width=50, height=80, anchor=SW)
l.pack()


img = PhotoImage(file='python-logo.png')
l_logo = Label(root, image=img)
l_logo.pack()


root.mainloop()
