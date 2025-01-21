from tkinter import*
import speech_recognition as sr
from tkinter.filedialog import asksaveasfile

def speech_translation():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        lis=rec.listen(source)
    try:
        converted=rec.recognize_google(lis)
        text_area.insert(END,converted)
    except:
        text_area.delete(1.0,END)
        text_area.insert(END,"Sorry the message was not clear...")

def s_file():
    file=asksaveasfile(defaultextension="*.txt")
    try:
        t=text_area.get(1.0,END)
        print(t,file=file)
    except:
        print("THIS CANNOT BE SAVED...")    


            

root=Tk()
root.geometry("500x300")
root.config(background="#bae1ff")

title=Label(root,font=("calibri",13),text="SPEECH TO TEXT!",background="#bae1ff")
title.pack()

record=Button(root,text="RECORD",command=speech_translation)
record.pack(pady=20,padx=20)

text_area=Text(root,width=30,height=5)
text_area.pack(pady=20)

save=Button(root,text="SAVE",width=20,command=s_file)
save.pack(pady=20)


root.mainloop()
