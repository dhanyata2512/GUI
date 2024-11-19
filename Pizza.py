from tkinter import*
from tkinter.ttk import*

pizza_varity=("Mushroom pizza","Spicy Veggie","Greek pizza","Farmhouse Pizza","Veg Extravaganza","Schezwan Margherita","Veggie Supreme","Neapolitan Pizza")

def final_result():
    p=pizza.get()
    s=p_size.get()
    a=amount.get()
    res="You have oredered a "+ a +", "+str(s)+" " +p + " pizza(s)"
    result.config(text=res)  
    

root=Tk()
root.title("Pizza Palace!")
root.config(background="#FE7EAA")

header=Label(root,text="Pizza Palace!",background="#FE7EAA",font=("calibri",20))
header.grid(row=0,column=0,columnspan=4,pady=23)


select_pizza=Label(root,text="Select your pizza:",background="#FE7EAA")
select_pizza.grid(row=1,column=0,columnspan=2)

pizza=StringVar()

pizza_type=Combobox(root,textvariable=pizza,values=pizza_varity)
pizza_type.grid(row=1,column=2,columnspan=2)

pizza_amount=Label(root,text="Enter Quantity:",background="#FE7EAA")
pizza_amount.grid(row=2,column=0,columnspan=2)

amount=Entry(root)
amount.grid(row=2,column=2)

pizza.set("Margherita")

p_size=StringVar()

options=Radiobutton(root,text="S",variable=p_size,value="S")
options.grid(row=1,column=4,padx=20,pady=10)

options_2=Radiobutton(root,text="M",variable=p_size,value="M")
options_2.grid(row=2,column=4,padx=10)

options_3=Radiobutton(root,text="L",variable=p_size,value="L")
options_3.grid(row=3,column=4,padx=10)

p_size.set(value="S")

generate=Button(root,text="Generate",command=final_result)
generate.grid(row=3,column=0,columnspan=4,pady=10)

result=Label(root,background="#FE7EAA")
result.grid(row=4,column=0)

root.mainloop()