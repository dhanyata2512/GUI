from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter import messagebox
import os

root=Tk()
root.geometry("600x400")
root.config(background="#FF82AB")

student_marks={}

def open_file():
    reset()
    global student_marks
    f=askopenfile(mode="r")
    if f is not None:
        student_marks=eval(f.read())
        for i in student_marks:
            l_box.insert(END,i)
        file_name=os.path.basename(f.name)
        title.config(text=file_name)



def s_file():
    file=asksaveasfile(defaultextension="*.txt")
    if file is not None:
            print(student_marks,file=file)
            reset()

def reset():
    clear_all()
    l_box.delete(0,END) 
    student_marks.clear() 
    title.config(text="Student Marks Logger")    

def adding():
    n=n_entry.get()
    if n == "":
        messagebox.showerror("Error","Name is mandatory!")
    else:
        if n not in student_marks:
            l_box.insert(END,n)

        student_marks[n]=(rn_entry.get(),mm_entry.get(),sm_entry.get(),p_entry.get())    
        clear_all()         

def clear_all():
    n_entry.delete(0,END)
    rn_entry.delete(0,END)
    mm_entry.delete(0,END)
    sm_entry.delete(0,END)
    p_entry.delete(0,END)

def display(event):
    top_root=Toplevel(root)
    index_value=l_box.curselection()
    if index_value:
        name=l_box.get(index_value)
        details=student_marks[name]
        res1="Name:  "+name+ "\n" +"Roll Number:  "+details[0]+"\n"+"Maths Marks:  "+details[1]+"\n"+"Science Marks:  "+details[2]+"\n"+"Percentage:  "+"\n"+details[3]   
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
        details=student_marks[n]
        sm_entry.insert(END,details[0])
        mm_entry.insert(END,details[1])
        rn_entry.insert(END,details[2])
        p_entry.insert(END,details[3])        

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

sm_entry=Entry(right_frame)
sm_entry.grid(row=0,column=1)

m_mark=Label(right_frame,text="Maths marks:")
m_mark.grid(row=1,column=0,padx=20,pady=20)

mm_entry=Entry(right_frame)
mm_entry.grid(row=1,column=1)

percentage=Label(right_frame,text="Percentage:")
percentage.grid(row=2,column=0,padx=20)

p_entry=Entry(right_frame)
p_entry.grid(row=2,column=1)

bm_frame=Frame(root,background="#FF82AB")
bm_frame.pack()

s_bar=Scrollbar(bm_frame)
s_bar.grid(row=0,column=1)

l_box=Listbox(bm_frame,yscrollcommand=s_bar.set,width=70)
l_box.grid(row=0,column=0)
l_box.bind("<<ListboxSelect>>",display)

bottom_frame=Frame(root,background="#FF82AB")
bottom_frame.pack(pady=20)

edit=Button(bottom_frame,text="Edit",width=8,command=edit)
edit.grid(row=1,column=0)

delete=Button(bottom_frame,text="DELETE",width=8,command=remove)
delete.grid(row=1,column=1,padx=20)

open=Button(bottom_frame,text="OPEN",width=8,command=open_file)
open.grid(row=1,column=2)

add=Button(bottom_frame,text="UPDATE/ADD",command=adding)
add.grid(row=1,column=3,padx=20)

save=Button(bottom_frame,text= "SAVE",width=20,command=s_file)
save.grid(row=1,column=4)

s_bar.config(command=l_box.yview) 

root.mainloop()
