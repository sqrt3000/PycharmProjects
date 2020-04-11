import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import webbrowser
import time
import re
import cv2
import PIL.Image, PIL.ImageTk
from PIL import ImageTk, Image
from selenium.webdriver.chrome.options import Options
opts_chrome = Options()
opts_chrome.add_argument('-headless')
opts_chrome.add_argument('--start-maximized')
from selenium.webdriver.firefox.options import Options
opts_ff = Options()
opts_ff.add_argument('-headless')
opts_ff.add_argument('--start-maximized')

PROXY_HOST = '192.168.3.2'  # rotating proxy or host
PROXY_PORT = 8080 # port
PROXY_USER = 'proxy-user'   # username
PROXY_PASS = 'proxy-password'   # password

# path = str("./Screenshots/screenshot.png")


def get_screen(browser, opts, txt):
    display_clean()
    display(txt='Start process...')
    width_window = (entry_width.get())
    test_url = (tested_url.get())
    if not test_url:
        print('Set URL please!')
        messagebox.showwarning('Warning', 'Set URL please!')
        return
    if not width_window:
        print('Set width please!')
        messagebox.showwarning('Warning', 'Set width please!')
        return
    else:
        display(txt=f"Browser window width: {width_window} px")
    if width_window.isnumeric():
        pass
    else:
        print('Input digits only')
        messagebox.showwarning('Warning', "Input 'width browser' must be digits only!")
        return
    if int(width_window) > 7680 or int(width_window) < 320:
        messagebox.showwarning('Warning', 'Width must be <= 7680 px and >= 320 px')
        return
    print('**************************')
    print('Open browser')
    display(txt=f"Open browser {txt} (headless mode)")
    browser = browser(options=opts)
    browser.set_window_size(width_window, 0)
    if re.search(r'http', test_url):
        pass
    else:
        test_url = ('http://' + test_url)
    try:
        requests.get(test_url)
        correct_url = True
    except:
        print("Please enter a valid URL")
        browser.close()
        browser.quit()
        print('Close browser')
        messagebox.showwarning('Warning', 'Please enter a valid URL!')
        display(txt='Close browser')
        return
    if correct_url:
        print("Correct URL")
        display(txt='URL is correct')
    print('Get URl')
    display(txt='Getting page site...')
    browser.get(test_url)
    total_width = browser.execute_script("return document.body.offsetWidth")
    total_height = browser.execute_script("return document.body.scrollHeight")
    print('Scrolling...')
    display(txt='Scrolling page')
    browser.set_window_size(total_width, total_height+83)
    print('Set window size')
    print('Delay 2 s')
    display(txt='Delay 2s...')
    time.sleep(2)
    browser.find_element_by_tag_name('body').screenshot(f"screenshot_from_{txt}.png")
    print('Make screenshot and save it')
    display(txt='Make screenshot and save it')
    browser.close()
    display(txt='Close browser')
    browser.quit()
    print('Close browser')
    display(txt='Your screenshot saved in current directory  successful!')


def get_resolution(width):
    entry_width.delete(0, END)
    entry_width.insert(END, width)


def reset_configs():
    entry_width.delete(0, END)
    entry_width.insert(0, 1024)
    tested_url.delete(0, END)
    txt = 'Please enter a valid URL, choose at least one width, and click button FireFox or Chrome...'
    display_clean()
    display(txt)


def display(txt):
    mess.insert(END, txt+'\n')
    mess.see("end")
    mess.update()


def display_clean():
    mess.delete(0.0, END)


def close():
    root.destroy()
    root.quit()


root = ThemedTk(theme="arc")

#Get resolution current monitor
h_display = (root.winfo_screenheight())/4
w_display = (root.winfo_screenwidth())/3
#set window middle
root.geometry(f"500x400+{int(w_display)}+{int(h_display)}")
root.resizable(0, 0)
root.title('Comparium')
root.iconbitmap('favicon.ico')

f_menu = Frame(root, bg="#2A303A", height=40)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(expand=1)
l_menu = Label(text="Web application automated testing", bg="#2A303A", fg="#C6DEC1", font="Arial 18")
l_menu.place(relx=0.12, y=5)
#Set background
img = PhotoImage(file='pattern.png')
l_logo = Label(root, image=img, bg="#3772D6", fg="#C6DEC1")
l_logo.pack()

# top_frame = ttk.Frame(root)
tested_url = ttk.Entry()
tested_url.place(relx=0.35, rely=0.12, relwidth=0.6, relheight=0.1)
url_label = Label(text="Tested URL:", font="Arial 12 bold")
url_label.place(relx=0.05, rely=0.12, relwidth=0.285, relheight=0.1)

width_frame = ttk.Frame(root)
width_frame.place(relx=0.45, rely=0.4, relwidth=0.2, relheight=0.05, anchor='n')
entry_width = ttk.Entry()
entry_width.place(relx=0.56, relwidth=0.1, rely=0.4, relheight=0.05)
entry_width.insert(0, 1024)
entry_label = Label(width_frame, text="Browser width:   ", font="Arial 8 bold")
entry_label.grid()
entry_px = Label(text="(px)", font="Arial 8 bold")
entry_px.place(relx=0.67, rely=0.4, relwidth=0.05, relheight=0.05)

#Buttons init
img_btn_1 = PhotoImage(file='FF_logo.png')
# Resizing image to fit on button
img_btn_1 = img_btn_1.subsample(5, 5)
img_btn_2 = PhotoImage(file='Chrome_logo.png')
# Resizing image to fit on button
img_btn_2 = img_btn_2.subsample(4, 4)
img_btn_3 = PhotoImage(file='reset.png')
# # Resizing image to fit on button
img_btn_3 = img_btn_3.subsample(8, 8)
img_btn_width_1 = PhotoImage(file='320.png')
# Resizing image to fit on button
img_btn_width_1 = img_btn_width_1.subsample(2, 2)
img_btn_width_2 = PhotoImage(file='375.png')
# Resizing image to fit on button
img_btn_width_2 = img_btn_width_2.subsample(2, 2)
img_btn_width_3 = PhotoImage(file='414.png')
# Resizing image to fit on button
img_btn_width_3 = img_btn_width_3.subsample(2, 2)
img_btn_width_4 = PhotoImage(file='1024.png')
# Resizing image to fit on button
img_btn_width_4 = img_btn_width_4.subsample(2, 2)
img_btn_width_5 = PhotoImage(file='1112.png')
# Resizing image to fit on button
img_btn_width_5 = img_btn_width_5.subsample(2, 2)
img_btn_width_6 = PhotoImage(file='1366.png')
# Resizing image to fit on button
img_btn_width_6 = img_btn_width_6.subsample(2, 2)
img_btn_width_7 = PhotoImage(file='1920.png')
# Resizing image to fit on button
img_btn_width_7 = img_btn_width_7.subsample(1, 1)
button = ttk.Button(root, text="FireFox", command=lambda: get_screen(browser=Firefox, opts=opts_ff, txt='FireFox'), image=img_btn_1, compound=LEFT)
button.place(relx=0.63, rely=0.25, relwidth=0.2, relheight=0.1, anchor='n')
button = ttk.Button(root, text="Chrome", command=lambda: get_screen(browser=Chrome, opts=opts_chrome, txt='Chrome'), image=img_btn_2, compound=LEFT)
button.place(relx=0.85, rely=0.25, relwidth=0.2, relheight=0.1, anchor='n')
button = ttk.Button(root, command=reset_configs, image=img_btn_3)
button.place(relx=0.425, rely=0.25, relwidth=0.15, relheight=0.1, anchor='n')
button = ttk.Button(root, text="Get last screen", command=lambda: func(), compound=CENTER)
button.place(relx=0.85, rely=0.385, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="320 px", command=lambda: get_resolution(320), image=img_btn_width_1, compound=LEFT)
button.place(relx=0.15, rely=0.25, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="375 px", command=lambda: get_resolution(375), image=img_btn_width_2, compound=LEFT)
button.place(relx=0.15, rely=0.335, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="414 px", command=lambda: get_resolution(414), image=img_btn_width_3, compound=LEFT)
button.place(relx=0.15, rely=0.42, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="1024  px", command=lambda: get_resolution(1024), image=img_btn_width_4, compound=LEFT)
button.place(relx=0.15, rely=0.505, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="1112 px", command=lambda: get_resolution(1112), image=img_btn_width_5, compound=LEFT)
button.place(relx=0.15, rely=0.59, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="1366 px", command=lambda: get_resolution(1366), image=img_btn_width_6, compound=LEFT)
button.place(relx=0.15, rely=0.675, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="1440 px", command=lambda: get_resolution(1440), image=img_btn_width_7, compound=LEFT)
button.place(relx=0.15, rely=0.76, relwidth=0.2, relheight=0.075, anchor='n')
button = ttk.Button(root, text="1920 px", command=lambda: get_resolution(1920), image=img_btn_width_7, compound=LEFT)
button.place(relx=0.15, rely=0.845, relwidth=0.2, relheight=0.075, anchor='n')

#Настраиваем вывод консольных сообщений в область Text()
f_text = Label()
f_text.place(relx=0.35, rely=0.48, relwidth=0.6, relheight=0.4)
mess = Text(f_text, bg="#2A303A", fg='#00FF00', padx=4, pady=3, wrap=WORD, insertbackground="#EDA756",
         selectbackground="#4E5A65", width=1, spacing3=1)
mess.pack(fill=BOTH, expand=1, side=LEFT)
scroll = Scrollbar(f_text, command=mess.yview)
scroll.pack(fill=Y, side=LEFT)
mess.config(yscrollcommand=scroll.set)

#Set footer and link
link_label = Label(root, text="Visit our website: ", bg='#3772D6', font="Arial 10")
link_label.place(relx=0.42, rely=0.92)
link = Label(root, text="www.comparium.app", font="Arial 10", bg='#3772D6', fg="blue", cursor="hand2")
link.place(relx=0.63, rely=0.92)
link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))


def func():
    modal = Tk()
    # modal.iconbitmap('favicon.ico')

    # modal.transient(root)
    #top.grab_set()
    # modal.focus_set()
    # modal.wait_window()
    # cv_img = cv2.cvtColor(cv2.imread("screenshot_from_FireFox.png"), cv2.COLOR_BGR2RGB)
    # height, width, no_channels = cv_img.shape
    # canvas = tkinter.Canvas(modal, width=width, height=height)
    # canvas.pack()
    # # photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    # canvas.create_image(0, 0, image=cv_img)

    # canvas = Canvas(modal, width=300, height=300)
    # canvas.pack()
    # img = ImageTk.PhotoImage(Image.open(""))
    # canvas.create_image(20, 20, anchor=NW, image=img)

    image = Image.open("screenshot_from_FireFox.png")
    modal = ImageTk.PhotoImage(image)



reset_configs()
root.mainloop()


