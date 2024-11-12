from tkinter import*
from tkinter.ttk import*

def final_result():
    n=number.get()
    r=multiple.get()
    table=""
    for i in range(0,r+1):
      res=str(n)+"X"+str(i)+ "="+str(n*i)+"\n"
      table=table+res
    result.config(text=table)  

root=Tk()
root.title("Times Tables!")
root.config(background="#9DD6E7")

header=Label(root,text="Times Tables!",background="#9DD6E7",font=("calibri",20))
header.grid(row=0,column=0,columnspan=4,pady=23)


number_range=Label(root,text="Number and range-",background="#9DD6E7",font=10)
number_range.grid(row=1,column=0,columnspan=2)

number=IntVar()

numbers=Combobox(root,textvariable=number)
numbers["values"]=tuple(range(101))
numbers.grid(row=1,column=2,columnspan=2)

number.set(0)

multiple=IntVar()

options=Radiobutton(root,text=10,variable=multiple,value=10)
options.grid(row=2,column=1)

options_2=Radiobutton(root,text=20,variable=multiple,value=20)
options_2.grid(row=2,column=2)

options_3=Radiobutton(root,text=30,variable=multiple,value=30)
options_3.grid(row=2,column=3)

multiple.set(value=10)

generate=Button(root,text="Generate",command=final_result)
generate.grid(row=3,column=0,columnspan=4)

result=Label(root,background="#9DD6E7")
result.grid(row=4,column=0)

root.mainloop()
