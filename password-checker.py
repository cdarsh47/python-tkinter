from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Password checker/generator")
#root.geometry("400x400")

main_frame=LabelFrame(root,text="Password Generate frame",padx=5,pady=5)
main_frame.grid(row=1,column=0,padx=10,pady=10)

def generate_password():
	numbers=['0','1','2','3','4','5','6','7','8','9']
	lower_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	upper_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	special_list=['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','.']
	password_list=[]

	password_list=random.sample(lower_alphabets, 4)+random.sample(upper_alphabets, 4)+random.sample(numbers, 2)+random.sample(special_list, 2)
	random.shuffle(password_list)
	password_string = ''.join(map(str, password_list))
	Label(main_frame,text=' || ').grid(row=2,column=0)
	Label(main_frame,text=' || ').grid(row=3,column=0)
	Label(main_frame,text=password_string,bg="green",fg="#fff").grid(row=4,column=0)

gen_btn=Button(main_frame,text="Generate new password",command=lambda : generate_password())
gen_btn.grid(row=1,column=0)

def check_password(password_value):

	class check_strength:

		def __init__(self,pwd):
			print("in init")
			self.pwd=pwd

		def check_length(self):
			status=0
			if len(password_value) >= 12:
				status=1
			return status	

		def check_lower(self):
			status=0
			for char in self.pwd:
				if char.islower():
					status=1	
					break
			return status		
		
		def check_upper(self):
			status=0
			for char in self.pwd:
				if char.isupper():
					status=1	
					break
			return status

		def check_numeric(self):
			status=0
			for char in self.pwd:
				if char.isdigit():
					status=1
					break
			return status

		def check_specialchars(self):
			status=0
			special_list=['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','.']
			special_exists=[char for char in self.pwd if char in special_list]
			if special_exists:
				status=1
			return status

	chk_pwd=check_strength(password_value)

	pwd_pros,pwd_cons=[],[]

	if chk_pwd.check_length():
		pwd_pros.append("Your password has 12 or more characters")
	else:
		pwd_cons.append("Your password have less than 12 characters")

	if chk_pwd.check_lower():
		pwd_pros.append("Your password has lowercase character")
	else:
		pwd_cons.append("Your password does not have lowercase character")

	if chk_pwd.check_upper():
		pwd_pros.append("Your password has uppercase character")
	else:
		pwd_cons.append("Your password does not have uppercase character")

	if chk_pwd.check_numeric():
		pwd_pros.append("Your password has a number")
	else:
		pwd_cons.append("Your password does not have a number")			
		
	if chk_pwd.check_specialchars():
		pwd_pros.append("Your password has a special character")
	else:
		pwd_cons.append("Your password does not have a special character")

	i=4	
	if pwd_pros:
		for x,stmt in enumerate(pwd_pros,1):
			Label(root,text=str(x)+') '+stmt).grid(row=i,column=0)
			i += 1
	j=4
	if pwd_cons:
		for x,stmt in enumerate(pwd_cons,1):
			Label(root,text=str(x)+') '+stmt).grid(row=j,column=3)
			j+=1			


password_input=Entry(root,width=30,fg="#000",borderwidth="5")
password_input.grid(row=3,column=0)

check_btn=Button(root,text="check my password",command=lambda : check_password(password_input.get()))
check_btn.grid(row=3,column=2)

root.mainloop()


