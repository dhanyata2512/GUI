from tkinter import*

root=Tk()
root.geometry("400x300")

label_1=Label(root,text="Chocos and Chocolate Ice-Cream")
label_1.pack()

top_frame=Frame(root)
top_frame.pack()

button_1=Button(top_frame,text="Choco")
button_1.pack(side="left")

button_2=Button(top_frame,text="Dark Chocolate")
button_2.pack(side="left")

button_3=Button(top_frame,text="Flake 99")
button_3.pack(side="left")


bottom_frame=Frame(root)
bottom_frame.pack(pady=30)

button_4=Button(bottom_frame,text="mint Ice-Cream")
button_4.pack(side="bottom")

button_5=Button(bottom_frame,text="Mango Ice-cream")
button_5.pack(side="bottom")

button_6=Button(bottom_frame,text="Bubble-gum Ice-cream")
button_6.pack(side="bottom")

root.mainloop()