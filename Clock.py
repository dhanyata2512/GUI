from tkinter import*
from time import strftime

def time():
    text_display=strftime("%H : %M : %S")
    text_date=strftime("%A %d %B %Y")
    clock.config(text=text_display)
    date.config(text=text_date)
    clock.after(1000,time)

root=Tk()
#root.geometry("400x170")
root.title("Clock")
root.config(background="#d0d0fe")

top_frame=Frame(root,background="#FFC09F")
top_frame.pack(padx=20,pady=20)

clock=Label(top_frame,background="#FFC09F",font=("calibri",32))
clock.grid(row=0,column=0)
date=Label(top_frame,background="#FFC09F",font=("calibri",23))
date.grid(row=1,column=0)

time()
root.mainloop()
