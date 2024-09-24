from tkinter import *

def convert():
    celsius=number_box.get()
    if celsius.replace(".","",1).isdigit():
        celsius=float(celsius)
        fahrenheit=celsius*1.8+32
        label_3.config(text=str(fahrenheit))
        label_3.grid(row=0,column=0,pady=10)

    else:
        label_4.config(text="Enter a valid NUMBER")
        label_4.grid(row=0, column=0)
root=Tk()

root.geometry("460x300")

root.title("Login Page")
root.config(background="light blue")

label_1=Label(root,text="Celsius  --> Fahrenheit",font="stencil",bd=7,background="#DDA0DD")
label_1.pack(padx=30,pady=20)

top_frame=Frame(root,background="light blue")
top_frame.pack(padx=30,pady=20)

label_2=Label(top_frame,text="Enter temprature in Celsius:",font="Arial",background="#DDA0DD")
label_2.grid(row=0,column=0)

number_box=Entry(top_frame)
number_box.grid(row=0,column=1,padx=10)

bottom_frame=Frame(root,background="light blue")
bottom_frame.pack(pady=20,padx=30)

label_3=Label(bottom_frame,font="Arial", background="#DDA0DD")

label_4=Label(bottom_frame,font="Ariial",background= "#DDA0DD")

convert_2=Button(bottom_frame,text=" Convert ", background="#DDA0DD",bd=6,command=convert)
convert_2.grid(row=2,column=0,pady=10)


root.mainloop()
