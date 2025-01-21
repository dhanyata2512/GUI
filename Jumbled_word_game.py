from tkinter import*

root=Tk()
root.geometry("450x320")
root.config(background="#EE6193")

my_words=["CAKES","COOKIES","BISCUITS","PASTRIES","CANDIES","CANDIES","PUDDINGS","CUSTARD","DEEP FRIED","ICE CREAM","JELLY","PIE","CHEESECAKE","BROWNIES","S'MORES","LEMMON SQUARE","CHURROS","FUDGE","CHOCLATE"]

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

check=Button(bottom_frame,text="Check",font=("calibri",15),foreground="#6193EE")
check.grid(row=5,column=0)

reset=Button(bottom_frame,text="Reset",font=("calibri",15),foreground="#0c6c32")
reset.grid(row=7,column=0,pady=30)

root.mainloop()