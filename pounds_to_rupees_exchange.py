from tkinter import*
import tkinter.font as font 

def conversion():
    pound=float(pounds.get())
    r=round(pound*109.89,2)
    rupee.config(text=r)
    

root=Tk()
root.geometry("460x300")

root.title("Pounds to rupees")
root.config(background="#FFabc0")

my_font=font.Font(family="Georgia")

heading=Label(root,text=" £ to ₹ ",font="Grumpy",bd=7,background="#abc0ff")
heading.pack(padx=30,pady=20)

top_frame=Frame(root,background="#FFabc0")
top_frame.pack(padx=30,pady=9)

input_label=Label(top_frame,text="Enter the currency in £: ",font=my_font,background="#abc0ff")
input_label.grid(row=0,column=0)

pounds=Entry(top_frame)
pounds.grid(row=0,column=1,padx=10)

convert_button=Button(top_frame,text="Covert",font=my_font,background="#abc0ff", command=conversion)
convert_button.grid(row=1,column=0,columnspan=2,pady=20)

bottom_frame=Frame(root,background="#FFabc0")
bottom_frame.pack(padx=30)

rupees_label=Label(bottom_frame,text="Rupees(₹):",font=my_font,background="#abc0ff")
rupees_label.grid(row=0,column=0,padx=5)

rupee=Label(bottom_frame,font=my_font,background="#FFabc0")
rupee.grid(row=1,column=0,padx=5)


root.mainloop()