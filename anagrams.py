from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Check Anagrams Program")

Label(root,text="===========================================").grid(row=0,column=0,columnspan=3)
Label(root,text="Please enter the strings in the below fields.").grid(row=1,column=0,columnspan=3)
Label(root,text="===========================================").grid(row=2,column=0,columnspan=3)

def check_anagram(str1_value,str2_value):
	value1 = str1_value.replace(' ', '')
	value2 = str2_value.replace(' ', '')
	result=Label(root,text="Congrats The Entered strings are Anagrams!!",bg="#fff",fg="#fff").grid(row=6,column=0,columnspan=3)

	if set(value1) == set(value2):
		result=Label(root,text="Congrats The Entered strings are Anagrams!!",bg="green",fg="#fff").grid(row=6,column=0,columnspan=3)
	else:
		result=Label(root,text="The Entered strings are not Anagrams!",bg="red",fg="#fff").grid(row=6,column=0,columnspan=3)

e1_name = Entry(root,width=30,fg="#0000ff",borderwidth="5")
e1_name.grid(row=3,column=0,columnspan=3)
e1_name.insert(0,"Please enter the first string:")

e2_name = Entry(root,width=30,fg="#0000ff",borderwidth="5")
e2_name.grid(row=4,column=0,columnspan=3)
e2_name.insert(0,"Please enter the second string:")

submit_button=Button(root,text="CHECK !!",fg="#fff",bg="#333",command=lambda: check_anagram(e1_name.get(),e2_name.get()))
submit_button.grid(row=5,column=0,columnspan=3)

root.mainloop()