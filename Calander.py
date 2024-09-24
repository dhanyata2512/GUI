from tkinter import *
import calendar

def show_calender():
    c_screen=Tk()
    c_screen.title("Calander")
    c_screen.geometry("800x600")
    c_screen.config(background="light blue")

    year_c=int(year_box.get())
    info_c=calendar.calendar(year_c)
    display_c=Text(c_screen,height=600,width=800)
    display_c.insert(END,info_c)
    display_c.pack()

    c_screen.mainloop()

#GUI

root=Tk()

root.geometry("400x300")

root.title("Calanders")
root.config(background="light blue")

calander_a=Label(root,text="Calander",background="#FF9A8A",bd=5,font="stencil")
calander_a.place(x=130,y=20)

year=Label(root,text="Enter Year:",background="#FF9A8A",bd=3,font="stencil")
year.place(x=30,y=90)

year_box=Entry(root)
year_box.place(x=180,y=100)

submit=Button(root,text="Submit",bd=5,command=show_calender)
submit.place(x=160,y=140)

exit=Button(root,text="Exit",bd=5,background="#E6E6FA",command=exit)
exit.place(x=170,y=180)


root.mainloop()
