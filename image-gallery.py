from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Gallery")

my_img1 = ImageTk.PhotoImage(Image.open('--- IMAGE URL ---'))

my_img2 = ImageTk.PhotoImage(Image.open('--- IMAGE URL ---'))

my_img3 = ImageTk.PhotoImage(Image.open('--- IMAGE URL ---'))

my_img4 = ImageTk.PhotoImage(Image.open('--- IMAGE URL ---'))

my_img5 = ImageTk.PhotoImage(Image.open('--- IMAGE URL ---'))

image_list,image_number=[my_img1,my_img2,my_img3,my_img4,my_img5],0

my_label=Label(image=my_img1)

my_label.grid(row=1,column=0,columnspan=3)

status_txt="Image "+str(image_number+1)+" of "+str(len(image_list))

status=Label(root,text=status_txt,fg="#0000ff",bd=1,relief=SUNKEN,anchor=E)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def forward():
	global image_number,status,my_label,button_back

	length=len(image_list)-1

	if image_number < length:
		image_number += 1
	else:
		image_number = 0	
	
	my_label.grid_forget()
	
	my_label=Label(image=image_list[image_number])
	
	my_label.grid(row=1,column=0,columnspan=3)
	
	status_txt="Image "+str(image_number+1)+" of "+str(len(image_list))
	
	status=Label(root,text=status_txt,fg="#0000ff",bd=1,relief=SUNKEN,anchor=E)
	
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back():
	global image_number,status,my_label,button_back

	length=len(image_list)-1

	if image_number < 1:
		image_number=length
	else:
		image_number -= 1	

	my_label.grid_forget()
	
	my_label=Label(image=image_list[image_number])
	
	my_label.grid(row=1,column=0,columnspan=3)
	
	status_txt="Image "+str(image_number+1)+" of "+str(len(image_list))
	
	status=Label(root,text=status_txt,fg="#0000ff",bd=1,relief=SUNKEN,anchor=E)
	
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_back=Button(root,text="<<  PREVIOUS IMAGE",command=back,padx=40,pady=10,bg="#00ff00",fg="#000",borderwidth=3)

button_exit=Button(root,text="EXIT PROGRAM",padx=40,pady=10,borderwidth=3,bg="#000000",fg="#ffffff",command=root.quit)

button_forward=Button(root,text="NEXT IMAGE  >>",padx=40,pady=10,bg="#00ff00",fg="#000",borderwidth=3,command=forward)

button_back.grid(row=0,column=0)

button_exit.grid(row=0,column=1)

button_forward.grid(row=0,column=2)

root.mainloop()