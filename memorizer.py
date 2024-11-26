from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile

root=Tk()
root.geometry("500x230")
root.config(background="#ff8da1")

def code():
    f=askopenfile(mode="r")
    if f is not None:
        p=f.read()
        print(p)

def s_file():
    asksaveasfile(defaultextension="*.txt")

def adding():
    i=input.get()
    l_box.insert(END,i)
    input.delete(0,END)

def remove():
    recive=l_box.curselection()
    for i in recive:  
        l_box.delete(i)

top_frame=Frame(root,background="#ff8da1")
top_frame.pack()       

save=Button(top_frame,text= "SAVE",command=s_file,width=8)
save.grid(row=0,column=0)

input=Entry(top_frame)
input.grid(row=1,column=0,pady=5)

add=Button(top_frame,text="ADD",width=8,command=adding)
add.grid(row=2,column=0)

bottom_frame=Frame(root,background="#ff8da1")
bottom_frame.pack(pady=10)

open=Button(bottom_frame,text="OPEN",command=code,width=8)
open.grid(row=0,column=0,padx=30)

delete=Button(bottom_frame,text="DELETE",width=8,command=remove)
delete.grid(row=0,column=3,padx=30)

s_bar=Scrollbar(bottom_frame)
s_bar.grid(row=0,column=2)

l_box=Listbox(bottom_frame,yscrollcommand=s_bar.set,selectmode=("multiple"))
l_box.grid(row=0,column=1)

s_bar.config(command=l_box.yview) 

root.mainloop()