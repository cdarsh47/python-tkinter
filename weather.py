from tkinter import *
import requests,json
from tkinter import messagebox

root=Tk()
root.title('weather')
root.configure(bg="green")

myLabel=Label(root,text="Welcome to the weather information.",bg="green",fg="#fff",font=("Helvetica",10)).grid(row=0,column=0,columnspan=3)
myCity = Entry(root,width=30,fg="#0000ff",borderwidth="3")
myCity.grid(row=1,column=0,columnspan=4)

def get_weather():
	city=myCity.get()

	if city:
		api_key='-- API KEY --'
		url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

		response=requests.get(url)
		result=json.loads(response.content)

		main_weather=result['weather'][0]['main']
		description=result['weather'][0]['description']
		main_temp=str(result.get("main").get("temp"))
		min_temp=str(result.get("main").get("temp_min"))
		max_temp=str(result.get("main").get("temp_max"))

		header="""The weather of """+city+""" is """+description+""". \n Information: """+main_weather+""". \n Temperature: """+main_temp+""". \n Maximum temperature: """+min_temp+""". \n Minimum temperature: """+max_temp+""". \n """
		weather_detail=Label(root,text=header,font=("Helvetica",10),fg="#fff",bg="green")
		weather_detail.grid(row=2,column=0,columnspan=4)
	else:
		messagebox.showwarning("Empty Value","Please enter some text!!")		

myButton=Button(root,text="Submit",command=get_weather,fg="#000",bg="#ccc").grid(row=2,column=1)

root.mainloop()