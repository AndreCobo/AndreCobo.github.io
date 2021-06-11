#!/usr/bin/python


# pip install bs4

# pip install requests


from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime
from datetime import date
import requests
from bs4 import BeautifulSoup

global cont

def quit(*args):
    root.destroy()
    
def show_time():
    if datetime.datetime.now().second%2==0:
        cont=True
    else:
        cont=False

    if datetime.date.today().day<10:
        day='0'+str(datetime.date.today().day)
    else:
        day=str(datetime.date.today().day)
        
    if datetime.date.today().month<10:
        month='0'+str(datetime.date.today().month)
    else:
        month=str(datetime.date.today().month)
        
    year=str(datetime.date.today().year)
    
    hour=str(datetime.datetime.now().hour)
    
    if datetime.datetime.now().minute<10:
        minute='0'+str(datetime.datetime.now().minute)
    else:
        minute=str(datetime.datetime.now().minute)
    
    if cont:
        txt_sep.set(':')
    else:
        txt_sep.set(' ')
    txt_hour.set(hour)
    txt_minute.set(minute)
    txt_date.set(day+'/'+month+'/'+year)
    
    url = 'https://andrecobo.github.io/aviso.html'    
    reqs = requests.get(url)
    
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    #print("Title of the website is : ")
    for title in soup.find_all('h1'):
        txt_notice1.set(title.get_text())
    for title in soup.find_all('h2'):
        txt_notice2.set(title.get_text())
    for title in soup.find_all('h3'):
        txt_notice3.set(title.get_text())
    
    root.after(1000, show_time)

# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

# Set the end date and time for the countdown

fnt_date = font.Font(family='Helvetica', size=60, weight='bold')
txt_date = StringVar()
lbl_date = ttk.Label(root, textvariable=txt_date, font=fnt_date, foreground="white", background="black")
lbl_date.place(relx=0.5, rely=0.5, anchor=CENTER)

fnt_big = font.Font(family='Helvetica', size=200, weight='bold')
txt_sep = StringVar()
lbl_sep = ttk.Label(root, textvariable=txt_sep, font=fnt_big, foreground="white", background="black")
lbl_sep.place(relx=0.5, rely=0.2, anchor=CENTER)
txt_hour = StringVar()
lbl_hour = ttk.Label(root, textvariable=txt_hour, font=fnt_big, foreground="white", background="black")
lbl_hour.place(relx=0.25, rely=0.2, anchor=CENTER)
txt_minute = StringVar()
lbl_minute = ttk.Label(root, textvariable=txt_minute, font=fnt_big, foreground="white", background="black")
lbl_minute.place(relx=0.75, rely=0.2, anchor=CENTER)


fnt_notice = font.Font(family='Helvetica', size=35, weight='bold')
txt_notice1 = StringVar()
lbl_notice1 = ttk.Label(root, textvariable=txt_notice1, font=fnt_notice, foreground="white", background="black")
lbl_notice1.place(relx=0.5, rely=0.7, anchor=CENTER)
txt_notice2 = StringVar()
lbl_notice2 = ttk.Label(root, textvariable=txt_notice2, font=fnt_notice, foreground="white", background="black")
lbl_notice2.place(relx=0.5, rely=0.8, anchor=CENTER)
txt_notice3 = StringVar()
lbl_notice3 = ttk.Label(root, textvariable=txt_notice3, font=fnt_notice, foreground="white", background="black")
lbl_notice3.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()