from tkinter import*
import random
from tkinter import messagebox

computer=random.randint(1,20)
  
def game():
    player=int(input_number.get())

    if player==computer:
        messagebox.showinfo("Information","Great job! :)")
        exit()

    elif player < computer:
        messagebox.showinfo("Information","Your guess is too low!") 
        input_number.delete(0,END) 

    else:
        messagebox.showinfo("Information","Your guess is too high!")
        input_number.delete(0,END)             
    
root=Tk()
root.geometry("460x300")

root.title("Guessing game!  :)")
root.config(background="#f291ad")

heading=Label(root,text="Guess the number!",font=("Grumpy",16),background="#ffe085")
heading.pack()


top_frame=Frame(root,background="#f291ad")
top_frame.pack()

number=Label(top_frame,text="Enter your number:",background="#ffe085",)
number.grid(row=0,column=0,pady=40)

input_number=Entry(top_frame)
input_number.grid(row=0,column=1,padx=10)

#AFEEEE
bottom_frame=Frame(root,background="#f291ad")
bottom_frame.pack(pady=20)


submit=Button(bottom_frame,text="submit",background="#88c4e7",command=game)
submit.grid(row=2,column=1,padx=20)


root.mainloop()