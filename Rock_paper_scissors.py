from tkinter import*
import random

player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

def choice(player_input):
    global player_score, computer_score

    computer_input=random.choice(choices)

    if(player_input == computer_input):
        winning.config(text = "Tie")
    elif (player_input=="rock" and computer_input =="scissors") or (player_input== "scissors" or computer_input == "paper") or (player_input== "paper" or computer_input == "rock"):
        winning.config(text="You Win! :)")
        player_score= player_score + 1

    else:
        winning.config(text="You Lose! :(")
        computer_score=computer_score - 1


    you_selected.config(text = 'Your Selected : ' + player_input)
    computer_selected.config(text = 'Computer Selected : ' + computer_input)
    you_score.config(text="Your Score:" + str(player_score))
    computer_score.config(text="Computer Score:" + str(computer_score))



root=Tk()
root.geometry("460x300")

root.title("Rock, Paper and scissors")
root.config(background="#bfb9ff")

heading=Label(root,text="Rock, Paper and Scissors",font=("Grumpy",16),background="#feffbe")
heading.pack()

winning=Label(root,font="Grumpy",background="#bfb9ff")
winning.pack()

top_frame=Frame(root,background="#bfb9ff")
top_frame.pack()

options=Label(top_frame,text="Your Options:",background="#feffbe",)
options.grid(row=0,column=0)

rock_button=Button(top_frame,text="Rock",background="#afe9ff",width=6, command=lambda:choice(choices[0]))
rock_button.grid(row=1,column=1,padx=30)

paper_button=Button(top_frame,text="Paper",background="#ffcfea",width=6,command=lambda:choice(choices[1]))
paper_button.grid(row=1,column=2)

scissors_button=Button(top_frame,text="Scissors",background="#cbffe6",width=6, command=lambda:choice(choices[2]))
scissors_button.grid(row=1,column=3,padx=30)

bottom_frame=Frame(root,background="#bfb9ff")
bottom_frame.pack(pady=20)

score_label=Label(bottom_frame,text="Score:",background="#feffbe",)
score_label.grid(row=0,column=0)

you_selected=Label(bottom_frame,text="Your Selected:",background="#bfb9ff")
you_selected.grid(row=1,column=1,pady=20)

computer_selected=Label(bottom_frame,text="Computer Selected:",background="#bfb9ff")
computer_selected.grid(row=2,column=1)

you_score=Label(bottom_frame,text="Your Score:",background="#bfb9ff")
you_score.grid(row=1,column=2, pady=20)

computer_score=Label(bottom_frame,text="Computer Score:",background="#bfb9ff")
computer_score.grid(row=2,column=2, padx=20)

root.mainloop()
