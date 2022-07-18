from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Palindrome Program")

Label(root,text="===========================================").grid(row=0,column=0,columnspan=3)
Label(root,text="Please enter the string in the below field.").grid(row=1,column=0,columnspan=3)
Label(root,text="===========================================").grid(row=2,column=0,columnspan=3)

def check_palindrome(str_value):
	response_string = str_value.replace(' ', '').lower()
	copy_string=response_string[::-1]

	if response_string == copy_string:
		Label(root,text="Congrats The Entered string is Palindrome!!",bg="green",fg="#fff").grid(row=4,column=0,columnspan=3)
	else:
		Label(root,text="The Entered string is not a Palindrome!!",bg="red",fg="#fff").grid(row=4,column=0,columnspan=3)

e_name = Entry(root,width=30,fg="#0000ff",borderwidth="5")
e_name.grid(row=3,column=0)
e_name.insert(0,"Please enter the string:")

submit_button=Button(root,text="CHECK !!",fg="#fff",bg="#333",command=lambda: check_palindrome(e_name.get()))
submit_button.grid(row=3,column=1)

root.mainloop()