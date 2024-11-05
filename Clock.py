from tkinter import*
from time import strftime
import random

def time():
    text_display=strftime("%H : %M : %S")
    text_date=strftime("%A %d %B %Y")
    random_colour=random.choice(background)
    top_frame.config(background=random_colour)    
    clock.config(text=text_display,background=random_colour)
    date.config(text=text_date,background=random_colour)
    clock.after(1000,time)

background= ["#F6A99F","#F9F0E3","#A5D5DA", "#CFEEDC", "#F5BCBC", "#DDD6F8", "#C2E5F0", "#9DD6E7", "#FE7EAA", "#77cbda", "#ff8da1", "#fdfbd4"]

root=Tk()
#root.geometry("400x170")
root.title("Clock")
root.config(background="#d0d0fe")

top_frame=Frame(root,background="#FCF7ED")
top_frame.pack(padx=20,pady=20)

clock=Label(top_frame,background="#FCF7ED",font=("calibri",32))
clock.grid(row=0,column=0)
date=Label(top_frame,background="#FCF7ED",font=("calibri",23))
date.grid(row=1,column=0)

time()
root.mainloop()
