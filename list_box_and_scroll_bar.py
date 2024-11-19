from tkinter import*

root=Tk()
root.geometry("400x300")

#getting scroll bar
s_bar=Scrollbar(root)
s_bar.pack(side=RIGHT,fill=Y)

#getting list box
l_box=Listbox(root,yscrollcommand=s_bar.set)
l_box.pack()
for i in range(25,):
    l_box.insert(END,str(i)+". Dark chocolate")

s_bar.config(command=l_box.yview) 

root.mainloop()