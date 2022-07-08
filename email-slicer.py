from tkinter import *
import re
from tkinter import messagebox

root = Tk()
root.title('Email Slicer.')
root.configure(bg="black")

label_win = Label(root,text="Welcome to email slicer program",font=("Helvetica",15),bg="#ff8000")
label_win.grid(row=0,column=0)

email_id = Entry(root,width=30)
email_id.grid(row=1,column=0,padx=10,pady=10)

def slice_func():
	email_value=email_id.get()

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if re.fullmatch(regex,email_value):

		sliced=email_value.split('@')
		
		label_user=Label(root,text="Your username is: "+sliced[0]+"",bg="black",fg="#00e054",font=("Arial",15))
		
		label_user.grid(row=3,column=0,padx=5,pady=5)
		
		label_domain=Label(root,text="Your email domain is: "+sliced[1]+"",bg="black",fg="#40bcf4",font=("Arial",15))
		
		label_domain.grid(row=4,column=0,padx=5,pady=5)			
	else:
		messagebox.showwarning("Invalid Value","Please enter proper email address!!")

submit=Button(root,text="slice it!!",height=2,width=15,command=slice_func)
submit.grid(row=2,column=0)

root.mainloop()