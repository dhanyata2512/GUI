from tkinter import*
import tkinter.font as font 

def conversion():
    kilogram=float(kg.get())
    g=round(kilogram*1000,2)
    p=round(kilogram*2.20462,2)
    o=round(kilogram*35.274,2)
    grams.config(text=g)
    pounds.config(text=p)
    ounces.config(text=o)
    

root=Tk()
root.geometry("460x300")

root.title("Weight Converter")
root.config(background="#D8EEDF")

my_font=font.Font(family="Georgia")

heading=Label(root,text="Weight Converter ",font="stencil",bd=7,background="#97D0ED")
heading.pack(padx=30,pady=20)

top_frame=Frame(root,background="#D8EEDF")
top_frame.pack(padx=30,pady=9)

input_label=Label(top_frame,text="Enter Weight in Kg: ",font=my_font,background="#97D0ED")
input_label.grid(row=0,column=0)

kg=Entry(top_frame)
kg.grid(row=0,column=1,padx=10)

convert_button=Button(top_frame,text="Covert",font=my_font,background="#97D0ED", command=conversion)
convert_button.grid(row=1,column=0,columnspan=2,pady=20)

bottom_frame=Frame(root,background="#D8EEDF")
bottom_frame.pack(padx=30)

gram_label=Label(bottom_frame,text="Grams:",font=my_font,background="#97D0ED")
gram_label.grid(row=0,column=0,padx=5)

grams=Label(bottom_frame,font=my_font,background="#D8EEDF")
grams.grid(row=1,column=0,padx=5)

pounds_label=Label(bottom_frame,text="Pounds:",font=my_font,background="#97D0ED")
pounds_label.grid(row=0,column=1,padx=25)

pounds=Label(bottom_frame,font=my_font,background="#D8EEDF")
pounds.grid(row=1,column=1,padx=25)

ounce_label=Label(bottom_frame,text="Ounce:",font=my_font,background="#97D0ED")
ounce_label.grid(row=0,column=2, padx=5)

ounces=Label(bottom_frame,font=my_font,background="#D8EEDF")
ounces.grid(row=1,column=2,padx=5)


root.mainloop()