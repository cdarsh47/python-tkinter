from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def show_error():
	messagebox.showerror("Calculator Program","Please select the second number.")

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number))

def clear_val():
	e.delete(0,END)

def button_add():
	global f_num,math
	first_number=e.get()
	math='add'
	f_num = int(first_number)
	e.delete(0,END)

def button_subtract():
	global f_num,math
	first_number=e.get()
	math='sub'
	f_num = int(first_number)
	e.delete(0,END)

def button_multiply():
	global f_num,math
	first_number=e.get()
	math='mul'
	f_num = int(first_number)
	e.delete(0,END)		

def button_divide():
	global f_num,math
	first_number=e.get()
	math='divide'
	f_num = int(first_number)
	e.delete(0,END)

def button_equal():
	second_number=e.get()
	if not second_number:
		show_error()
	else:	
		e.delete(0,END)

		if math == 'add':
			e.insert(0,f_num + int(second_number))
		elif math == 'sub':
			e.insert(0,f_num - int(second_number))
		elif math == 'mul':
			e.insert(0,f_num * int(second_number))
		elif math == 'divide':
			e.insert(0,f_num / int(second_number))
		else:
			e.insert(0,"no operator.")			

#define buttons
button_1 = Button(root,text="1",padx=30,pady=10,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=30,pady=10,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=30,pady=10,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=30,pady=10,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=30,pady=10,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=30,pady=10,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=30,pady=10,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=30,pady=10,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=30,pady=10,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=30,pady=10,command=lambda: button_click(0))
button_add = Button(root,text="+",padx=30,pady=10,command=button_add)
button_equal = Button(root,text=" = ",padx=60,pady=10,command=button_equal)
button_clear = Button(root,text="Clear",padx=60,pady=10,command=clear_val)

button_subtract = Button(root,text="-",padx=30,pady=10,command=button_subtract) 
button_multiply = Button(root,text="*",padx=30,pady=10,command=button_multiply)
button_divide = Button(root,text="/",padx=30,pady=10,command=button_divide)

#show buttons on screen
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=3)
button_equal.grid(row=5,column=1,columnspan=3)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()