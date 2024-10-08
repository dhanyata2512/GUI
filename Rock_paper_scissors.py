from tkinter import*

root=Tk()
root.geometry("460x300")

root.title("Rock, Paper and scissors")
root.config(background="light blue")

heading=Label(root,text="Rock, Paper and Scissors",font=("Grumpy",16),background="pink")
heading.pack()

winning=Label(root,font="Grumpy",background="light blue")
winning.pack()

top_frame=Frame(root,background="light blue")
top_frame.pack()

options=Label(top_frame,text="Your Options:",background="pink")
options.grid(row=0,column=0)

rock_button=Button(top_frame,text="Rock",background="purple",width=6)
rock_button.grid(row=1,column=1,padx=30)

paper_button=Button(top_frame,text="Paper",background="purple",width=6)
paper_button.grid(row=1,column=2)

scissors_button=Button(top_frame,text="Scissors",background="purple",width=6)
scissors_button.grid(row=1,column=3,padx=30)

botton_frame=Frame(root,background="light blue")
botton_frame.pack(pady=20)

score_label=Label(botton_frame,text="Score:",background="pink")
score_label.grid(row=0,column=0)

you_selected=Label(botton_frame,text="You Selected:",background="pink")
you_selected.grid(row=1,column=1,pady=20)

computer_selected=Label(botton_frame,text="Computer Selected:",background="pink")
computer_selected.grid(row=2,column=1)

root.mainloop()