from tkinter import*
from tkinter.ttk import*

root=Tk()
root.title("Times Tables!")
root.config(background="#CFEEDC")

header=Label(root,text="Times Tables!",background="#CFEEDC")
header.pack()

number_range=Label(root,text="Number and Range-",background="#CFEEDC")
number_range.pack(padx=20,pady=20,side=LEFT)

number=IntVar()

numbers=Combobox(root,textvariable=number)
numbers["values"]=tuple(range(101))
numbers.pack()

number.set(0)

top_frame=Frame(root)
top_frame.pack()

range=IntVar()

options=Radiobutton(top_frame,text=10,variable=range,value=10)
options.grid(row=0,column=0)

options_2=Radiobutton(top_frame,text=20,variable=range,value=20)
options_2.grid(row=0,column=1)

options_3=Radiobutton(top_frame,text=30,variable=range,value=30)
options_3.grid(row=0,column=2)

range.set(value=10)

generate=Button(top_frame,text="Generate")
generate.grid(row=1,column=3)

root.mainloop()