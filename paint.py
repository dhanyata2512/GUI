from tkinter import*


root=Tk()
root.title("Paint with me...") 
root.config(background="#FFF1F0")

        
brushpen=Button(root,text="Brush-Pen")
brushpen.grid(row=0,column=0)

color=Button(root,text="Colour")
color.grid(row=0,column=1)

eraser=Button(root,text="Rubber")
eraser.grid(row=0,column=2)

slider=Scale(root,from_=1,to=10,orient=HORIZONTAL)
slider.grid(row=0,column=3)

drawing_screen=Canvas(root,background="white",width=500,height=500)
drawing_screen.grid(row=1,column=0,columnspan=4)

#initial setup
oldx=None
oldy=None
colour="black"
width=2
slider.set(width)
active_button=brushpen
active_button.config(relief=SUNKEN)

root.mainloop()