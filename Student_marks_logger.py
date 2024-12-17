from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import messagebox

root=Tk()
root.geometry("600x400")
root.config(background="#FF82AB")

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

def remove():
    recive=l_box.curselection()
    recive=recive[::-1]
    for i in recive:  
        l_box.delete(i)

top_frame=Frame(root,background="#FF82AB")
top_frame.pack() 

title =Label(top_frame,text="Student Report Log",background="#FF82AB")
title.grid(row=0,column=0)

middle_frame=Frame(root,background="#FF82AB")
middle_frame.pack()

left_frame=Frame(middle_frame,background="#FF82AB")
left_frame.pack(side=LEFT,pady=20)

name=Label(left_frame,text="Name:")
name.grid(row=0,column=0,padx=20)

n_entry=Entry(left_frame)
n_entry.grid(row=0,column=1)

rollnumber=Label(left_frame,text="Rollnumber")
rollnumber.grid(row=1,column=0,padx=20,pady=20)

rn_entry=Entry(left_frame)
rn_entry.grid(row=1,column=1)

right_frame=Frame(middle_frame,background="#FF82AB")
right_frame.pack(side=LEFT,pady=20)

s_mark=Label(right_frame,text="Science marks:")
s_mark.grid(row=0,column=0,padx=20)

s_entry=Entry(right_frame)
s_entry.grid(row=0,column=1)

m_mark=Label(right_frame,text="Maths marks:")
m_mark.grid(row=1,column=0,padx=20,pady=20)

m_entry=Entry(right_frame)
m_entry.grid(row=1,column=1)

percentage=Label(right_frame,text="Percentage:")
percentage.grid(row=2,column=0,padx=20)

percentage_entry=Entry(right_frame)
percentage_entry.grid(row=2,column=1)

bm_frame=Frame(root,background="#FF82AB")
bm_frame.pack()

s_bar=Scrollbar(bm_frame)
s_bar.grid(row=0,column=1)

l_box=Listbox(bm_frame,yscrollcommand=s_bar.set,width=70)
l_box.grid(row=0,column=0)

bottom_frame=Frame(root,background="#FF82AB")
bottom_frame.pack(pady=20)

edit=Button(bottom_frame,text="Edit",width=8)
edit.grid(row=1,column=0)

delete=Button(bottom_frame,text="DELETE",width=8,command=remove)
delete.grid(row=1,column=1,padx=20)

open=Button(bottom_frame,text="OPEN",command=open_file,width=8)
open.grid(row=1,column=2)

add=Button(bottom_frame,text="UPDATE/ADD")
add.grid(row=1,column=3,padx=20)

save=Button(bottom_frame,text= "SAVE",command=s_file,width=20)
save.grid(row=1,column=4)

s_bar.config(command=l_box.yview) 

root.mainloop()