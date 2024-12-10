from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import messagebox

root=Tk()
root.geometry("450x470")
root.config(background="#C2E5F0")

address_book={}

def open_file():
    f=askopenfile(mode="r")
    if f is not None:
        p=f.readlines()
        print(p)
        l_box.delete(0,END)
        for i in p:
            l_box.insert(END,i)

def s_file():
    file=asksaveasfile(defaultextension="*.txt")
    if file is not None:
        for item in l_box.get(0,END):
            print(item,file=file)
        l_box.delete(0,END)    


def adding():
    n=n_entry.get()
    if n == "":
        messagebox.showerror("Error","Name is mandatory!")

def remove():
    recive=l_box.curselection()
    recive=recive[::-1]
    for i in recive:  
        l_box.delete(i)


top_frame=Frame(root,background="#C2E5F0")
top_frame.pack()       

title =Label(top_frame,text="My Address Book",background="#C2E5F0")
title.grid(row=0,column=0)

open=Button(top_frame,text="OPEN",command=open_file,width=8)
open.grid(row=0,column=1,padx=30)

middle_frame=Frame(root,background="#C2E5F0")
middle_frame.pack()

left_frame=Frame(middle_frame,background="#C2E5F0")
left_frame.pack(side=LEFT,pady=20)

s_bar=Scrollbar(left_frame)
s_bar.grid(row=0,column=1)

l_box=Listbox(left_frame,yscrollcommand=s_bar.set,selectmode=("multiple"))
l_box.grid(row=0,column=0)

right_frame=Frame(middle_frame,background="#C2E5F0")
right_frame.pack(side=LEFT,pady=20)

name=Label(right_frame,text="Name:")
name.grid(row=0,column=0,padx=20)

n_entry=Entry(right_frame)
n_entry.grid(row=0,column=1)

address=Label(right_frame,text="Address:")
address.grid(row=1,column=0,padx=20,pady=20)

a_entry=Entry(right_frame)
a_entry.grid(row=1,column=1)

mobile=Label(right_frame,text="Mobile:")
mobile.grid(row=2,column=0,padx=20)

m_entry=Entry(right_frame)
m_entry.grid(row=2,column=1)

email=Label(right_frame,text="Email:")
email.grid(row=3,column=0,padx=20,pady=20)

e_entry=Entry(right_frame)
e_entry.grid(row=3,column=1)

birthday=Label(right_frame,text="Birthday:")
birthday.grid(row=4,column=0,padx=20)

b_entry=Entry(right_frame)
b_entry.grid(row=4,column=1)

bottom_frame=Frame(root,background="#C2E5F0")
bottom_frame.pack()

delete=Button(bottom_frame,text="DELETE",width=8,command=remove)
delete.grid(row=1,column=1,padx=10)

edit=Button(bottom_frame,text="Edit",width=8)
edit.grid(row=1,column=0)

add=Button(bottom_frame,text="ADD",width=8,command=adding)
add.grid(row=1,column=2)

save=Button(bottom_frame,text= "SAVE",command=s_file,width=32)
save.grid(row=6,column=1,pady=20)

s_bar.config(command=l_box.yview) 

root.mainloop()