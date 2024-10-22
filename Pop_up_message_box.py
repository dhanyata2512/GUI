from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("400x300")

#message box to show info

messagebox.showinfo("Information","Hello! How are you?")

#message box to show warning

messagebox.showwarning("Warning!!","Keep Away Dangrous Chemicals!!")

#message box to show error

messagebox.showerror("Error","Sorry, you have entered wrong information  :(")

#message box to ask a question (yes, no)

print(messagebox.askquestion("Question","Do you like dark choclate?"))

#message box to ask Ok or cancel

print(messagebox.askokcancel("Ok and cancel","Can I ask you a question?"))

#message box to ask  yes no(comes back with true or false)

print(messagebox.askyesno("YES NO",("Are you tired?")))

#message box to retry or cancel

print(messagebox.askretrycancel("retry or cancel", "Would you like to retry your question : 2+3"))

root.mainloop()