from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import messagebox
import os

root=Tk()
root.geometry("450x470")
root.config(background="#C2E5F0")

address_book={}

def open_file():
    reset()
    global address_book
    f=askopenfile(mode="r")
    if f is not None:
        address_book=eval(f.read())
        for i in address_book:
            l_box.insert(END,i)
        file_name=os.path.basename(f.name)
        title.config(text=file_name)



def s_file():
    file=asksaveasfile(defaultextension="*.txt")
    if file is not None:
            print(address_book,file=file)
            reset()

def reset():
    clear_all()
    l_box.delete(0,END) 
    address_book.clear() 
    title.config(text="My Address Book")        


def adding():
    n=n_entry.get()
    if n == "":
        messagebox.showerror("Error","Name is mandatory!")
    else:
        if n not in address_book:
            l_box.insert(END,n)

        address_book[n]=(a_entry.get(),m_entry.get(),e_entry.get(),b_entry.get())
        clear_all()

def clear_all():
    n_entry.delete(0,END)
    a_entry.delete(0,END)
    m_entry.delete(0,END)
    e_entry.delete(0,END)
    b_entry.delete(0,END)

def display(event):
    top_root=Toplevel(root)
    index_value=l_box.curselection()
    if index_value:
        name=l_box.get(index_value)
        details=address_book[name]
        res1="Name:  "+name+ "\n" +"Address:  "+details[0]+"\n"+"Mobile:  "+details[1]+"\n"+"Email:  "+details[2]+"\n"+"Birthday:  "+"\n"+details[3]   
        final_result=Label(top_root,text=res1)
        final_result.pack()

def remove():
    recive=l_box.curselection()
    recive=recive[::-1]
    for i in recive:  
        l_box.delete(i)

def edit():
    clear_all()
    index=l_box.curselection()
    if index:
        n=l_box.get(index)
        n_entry.insert(END,n)
        details=address_book[n]
        a_entry.insert(END,details[0])
        m_entry.insert(END,details[1])
        e_entry.insert(END,details[2])
        b_entry.insert(END,details[3])

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

l_box=Listbox(left_frame,yscrollcommand=s_bar.set)
l_box.grid(row=0,column=0)
l_box.bind("<<ListboxSelect>>",display)

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

edit=Button(bottom_frame,text="Edit",width=8,command=edit)
edit.grid(row=1,column=0)

add=Button(bottom_frame,text="ADD/UPDATE",width=12,command=adding)
add.grid(row=1,column=2)

save=Button(bottom_frame,text= "SAVE",command=s_file,width=32)
save.grid(row=6,column=1,pady=20)

s_bar.config(command=l_box.yview) 

root.mainloop()
