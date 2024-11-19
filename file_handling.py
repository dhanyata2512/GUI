from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile

root=Tk()
root.geometry("400x300")

def code():
    f=askopenfile(mode="r")
    if f is not None:
        p=f.read()
        print(p)

def s_file():
    asksaveasfile(defaultextension="*.txt")        

open=Button(root,text=" OPEN ",command=code)
open.pack()

save=Button(root,text= " SAVE ",command=s_file)
save.pack()


root.mainloop()
