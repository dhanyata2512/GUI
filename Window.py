from tkinter import *
#create a tkinter window
root=Tk()

#size the window (optional)
root.geometry('800x600')

#create a button
close=Button(root,text="Close",background="blue",foreground="white",bd="5",command=root.destroy)
close.pack(side="right")



#Runs the application (Shows the main window)
root.mainloop()