from tkinter import*
import random
from tkinter import messagebox

root=Tk()
root.geometry("450x320")
root.config(background="#EE6193")

word=""

def shuffler():
    my_words=["CAKES","COOKIES","BISCUITS","PASTRIES","CANDIES","CANDIES","PUDDINGS","CUSTARD","DOUGHNUT","ICE CREAM","JELLY","PIE","CHEESECAKE","BROWNIES","S'MORES","LEMMON SQUARE","CHURROS","FUDGE","CHOCLATE","TIRAMISU"]

    global word
    word=random.choice(my_words)

    separate_word=list(word)
    random.shuffle(separate_word)

    shuffled_words= ""
    for letters in separate_word:
        shuffled_words += letters

    jumble_word.config(text=shuffled_words)  

def answer():
    if word == w_entry.get():
        messagebox.showinfo("Congratulations","You are Correct! Please press 'Reset' to get another word...")
    else:
        messagebox.showerror("Sorry","The answer was Incorrect. Please try again...")

top_frame=Frame(root,background="#EE6193")
top_frame.pack()       

title =Label(top_frame,text="JUMBLED - UP WORD GAME! ",background="#EE6193",font=("stencil",20))
title.grid(row=0,column=0)

bottom_frame=Frame(root,background="#EE6193")
bottom_frame.pack(pady=30)


jumble_word=Label(bottom_frame,text="",background="#EE6193")
jumble_word.grid(row=0,column=0)

w_entry=Entry(bottom_frame,font=("calibri",13))
w_entry.grid(row=3,column=0,pady=30)

check=Button(bottom_frame,text="Check",font=("calibri",15),foreground="#6193EE",command=answer)
check.grid(row=5,column=0)

reset=Button(bottom_frame,text="Reset",font=("calibri",15),foreground="#0c6c32",command=shuffler)
reset.grid(row=7,column=0,pady=30)

shuffler()
root.mainloop()
