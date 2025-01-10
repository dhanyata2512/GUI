from tkinter import*
from gtts import gTTS
import os

def converts():
    tts=gTTS(text_input.get(),lang="hi")
    tts.save("convert.wav")
    os.system("convert.wav")

root=Tk()
root.geometry("400x220")
root.config(background="#A9E4DE")
root.title("Text to speech!")

top_frame=Frame(root,background="#A9E4DE")
top_frame.pack()

title=Label(top_frame,text="Text to Speech!",background="#A9E4DE")
title.pack()

bottom_frame=Frame(root,background="#A9E4DE")
bottom_frame.pack(pady=30)

text_input=Entry(bottom_frame,background="#A9E4DE",width=40)
text_input.pack()

convert=Button(bottom_frame,text="Convert",command=converts)
convert.pack(pady=20)


root.mainloop()