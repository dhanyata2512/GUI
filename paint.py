from tkinter import*
from tkinter.colorchooser import askcolor


root=Tk()
root.title("Paint with me...") 
root.config(background="#FFF1F0")

def activate_button(b_get,eraser_mode=False):
    global active_button, on_off_eraser
    active_button.config(relief=RAISED)
    active_button=b_get
    active_button.config(relief=SUNKEN)
    on_off_eraser=eraser_mode

def use_pen():
    activate_button(brushpen)

def use_eraser():
    activate_button(eraser,True)  

def use_color():
    global colour
    activate_button(color)   
    colour=askcolor(color=colour)[1] 
    print(colour)  

def draw(r_event):
    global colour, oldy,oldx
    if on_off_eraser == True:
        colour="white"
    if oldx and oldy:
        drawing_screen.create_line(oldx,oldy,r_event.x,r_event.y,width=slider.get(),fill=colour,splinesteps=50,capstyle=ROUND,smooth=True)    
    oldx=r_event.x
    oldy=r_event.y 

def reset(e):
    global oldx, oldy
    oldx=None
    oldy=None 


brushpen=Button(root,text="Brush-Pen",command=use_pen)
brushpen.grid(row=0,column=0)

color=Button(root,text="Colour",command=use_color)
color.grid(row=0,column=1)

eraser=Button(root,text="Rubber",command=use_eraser)
eraser.grid(row=0,column=2)

slider=Scale(root,from_=1,to=20,orient=HORIZONTAL)
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
on_off_eraser=False
drawing_screen.bind("<B1-Motion>",draw)
drawing_screen.bind("<ButtonRelease-1>",reset)
root.mainloop()
