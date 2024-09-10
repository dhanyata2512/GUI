from tkinter import *

root=Tk()

root.geometry("400x300")

#giving the screen a title and bg color 
root.title("Login Page")
root.config(background="light blue")

#Adding a labe(can't be changed by user)
username=Label(root,text="Username")
username.place(x=100,y=90)

password=Label(root,text="Password")
password.place(x=100,y=140)

#creating an entry widget

username_box=Entry(root)
username_box.place(x=170,y=90)

password_box=Entry(root,show="*")
password_box.place(x=170,y=140)

submit=Button(root,text="Submit",bd=5)
submit.place(x=130,y=180)



root.mainloop()