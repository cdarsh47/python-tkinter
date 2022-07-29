import pymysql.cursors,re
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Contact Book")

def database_conn():
	connection = pymysql.connect(host="localhost",user="root",password='',database='test',cursorclass=pymysql.cursors.DictCursor)

	db_object = connection.cursor()

	return db_object,connection

db_object,connection=database_conn()
db_object.execute("SELECT * FROM contact_book")
contacts=db_object.fetchall()

def restructure_grid():
	db_object,connection=database_conn()
	db_object.execute("SELECT * FROM contact_book")
	contacts=db_object.fetchall()
	main_frame=LabelFrame(root,text="Contact Records",padx=5,pady=5)
	main_frame.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

	i=1
	for contact in contacts:
		Label(main_frame,text=contact['id']).grid(row=i,column=0)
		Label(main_frame,text=contact['name']).grid(row=i,column=1)
		Label(main_frame,text=contact['contact_number']).grid(row=i,column=2)
		Label(main_frame,text=contact['email_id']).grid(row=i,column=3)
		Label(main_frame,text=contact['address']).grid(row=i,column=4)
		i+=1
	connection.commit()
	connection.close()	

main_frame=LabelFrame(root,text="Contact Records",padx=5,pady=5)
main_frame.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
i=1
for contact in contacts:
	Label(main_frame,text=contact['id']).grid(row=i,column=0)
	Label(main_frame,text=contact['name']).grid(row=i,column=1)
	Label(main_frame,text=contact['contact_number']).grid(row=i,column=2)
	Label(main_frame,text=contact['email_id']).grid(row=i,column=3)
	Label(main_frame,text=contact['address']).grid(row=i,column=4)
	i+=1
connection.commit()
connection.close()

def add_operation(name,number,email,address):

	db,connection=database_conn()

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

	if name and all(ch.isdigit() for ch in number) and re.fullmatch(regex,email) and address:

		Query='INSERT INTO contact_book(name,contact_number,email_id,address) values("'+name+'","'+str(number)+'","'+str(email)+'","'+address+'")'
		status = db.execute(Query)
		connection.commit()

		if status:
			messagebox.showinfo("Record Add","Record has been added successfully!!!!")
			main_frame.grid_forget()
			restructure_grid()
		else:
			messagebox.showwarning("Error","There seems to be some error.")
		connection.commit()	
		connection.close()
	else:
		messagebox.showwarning("Fields value error","Please fill the valid values in each field.")	

def del_operation(contact_id):
	db_object,connection=database_conn()

	response=messagebox.askyesno("Delete","Are you sure you want to delete the record?")
	if response==1:
		delete_sql = f"DELETE FROM contact_book WHERE id = {contact_id}"
		status=db_object.execute(delete_sql)
		if status:
			messagebox.showinfo("Deleted Record","Record has been deleted successfully!!!!")
		else:
			messagebox.showwarning("Error","There was some error.")
		connection.commit()
		connection.close()
		main_frame.grid_forget()
		restructure_grid()
	else:
		messagebox.showwarning("Value error","Please select valid mode.")

def update_record(contact_id,name,number,email,address):
	db,connection=database_conn()

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

	if name and all(ch.isdigit() for ch in number) and re.fullmatch(regex,email) and address:

		Query=f"UPDATE contact_book SET name='{name}',contact_number='{number}',email_id='{email}',address='{address}' WHERE id={contact_id}"
		status = db.execute(Query)		
		if status:
			messagebox.showinfo("Record updated","Record has been updated successfully!!!!")
			main_frame.grid_forget()
			restructure_grid()
		else:
			messagebox.showwarning("Error","There seems to be some error.")
		main_frame.grid_forget()
		restructure_grid()
		connection.commit()	
		connection.close()
	else:
		messagebox.showwarning("Fields value error","Please fill the valid values in each field.")

def edit_operation(contact_id):
	db_object,connection=database_conn()

	if all(ch.isdigit() for ch in contact_id):
		sql = f"SELECT * FROM contact_book WHERE id = {contact_id}"
		db_object.execute(sql)
		contact=db_object.fetchone()

		if contact:
			e_name = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
			e_name.grid(row=1,column=0)
			e_name.insert(0,contact['name'])
			e_number = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
			e_number.grid(row=1,column=1)
			e_number.insert(0,contact['contact_number'])
			e_email = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
			e_email.grid(row=1,column=2)
			e_email.insert(0,contact['email_id'])
			e_address = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
			e_address.grid(row=1,column=3)
			e_address.insert(0,contact['address'])
			edButton=Button(frame,text="Edit Record",command=lambda : update_record(contact['id'],e_name.get(),e_number.get(),e_email.get(),e_address.get()))
			edButton.grid(row=1,column=4)
	else:
		messagebox.showwarning("Value error","Please enter a valid value.")	
	connection.commit()
	connection.close()	

def perform_operation(mode):

	db_object,connection=database_conn()

	if mode == 'add':
		c_name = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		c_name.grid(row=1,column=0)
		c_name.insert(0,"Enter the name:")
		c_number = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		c_number.grid(row=1,column=1)
		c_number.insert(0,"Enter the number:")
		c_email = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		c_email.grid(row=1,column=2)
		c_email.insert(0,"Enter the email:")
		c_address = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		c_address.grid(row=1,column=3)
		c_address.insert(0,"Enter the address:")

		addButton=Button(frame,text="Add Record",command=lambda : add_operation(c_name.get(),c_number.get(),c_email.get(),c_address.get()))
		addButton.grid(row=1,column=4)
		connection.commit()
		connection.close()

	elif mode == 'delete':
		c_id = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		c_id.grid(row=2,column=0)
		c_id.insert(0,"Enter the record id:")

		delsub_btn=Button(frame,text="Delete",command=lambda: del_operation(c_id.get()))
		delsub_btn.grid(row=2,column=1)
	elif mode == 'edit':
		ec_id = Entry(frame,width=20,fg="#0000ff",borderwidth="5")
		ec_id.grid(row=2,column=0)
		ec_id.insert(0,"Enter the record id:")

		esub_btn=Button(frame,text="Edit",command=lambda: edit_operation(ec_id.get()))
		esub_btn.grid(row=2,column=1)			

frame=LabelFrame(root,text="Operation window",padx=5,pady=5)
frame.grid(row=i+1,column=0,padx=10,pady=10,columnspan=3)

addButton=Button(frame,text="Add a record",command=lambda : perform_operation('add'))
addButton.grid(row=0,column=0)

delButton=Button(frame,text="Delete a record",command=lambda : perform_operation('delete'))
delButton.grid(row=0,column=1)

edButton=Button(frame,text="Edit a record",command=lambda : perform_operation('edit'))
edButton.grid(row=0,column=2)

root.mainloop()