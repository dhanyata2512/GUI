from tkinter import*

root=Tk()
root.geometry("500x320")
root.config(background="#ff8da1")

def change_colour():
    recive=l_box.curselection()
    colour=l_box.get(recive)
    root.config(background=colour)
    top_frame.config(background=colour)
    bottom_frame.config(background=colour)

def starting_colours():
    l_box.insert(END,"Red")
    l_box.insert(END,"Orange")
    l_box.insert(END,"Yellow")
    l_box.insert(END,"Green")
    l_box.insert(END,"Light Green")

def adding():
    i=color_entry.get()
    l_box.insert(END,i)
    color_entry.delete(0,END)

def remove():
    recive=l_box.curselection()
    for i in recive:  
        l_box.delete(i)

top_frame=Frame(root,background="#ff8da1")
top_frame.pack()       


add=Button(top_frame,text= "ADD",command=adding,width=8)
add.grid(row=0,column=0)

color_entry=Entry(top_frame)
color_entry.grid(row=1,column=0,pady=5)

delete=Button(top_frame,text="DELETE",width=8,command=remove)
delete.grid(row=2,column=0)

bottom_frame=Frame(root,background="#ff8da1")
bottom_frame.pack(pady=10)

change_c=Button(bottom_frame,text="CHANGE COLOUR",width=15,command=change_colour)
change_c.grid(row=1,column=1,padx=30,pady=20)

s_bar=Scrollbar(bottom_frame)
s_bar.grid(row=0,column=2)

l_box=Listbox(bottom_frame,yscrollcommand=s_bar.set)
l_box.grid(row=0,column=1)

s_bar.config(command=l_box.yview)
starting_colours() 

root.mainloop()
