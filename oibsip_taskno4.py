# Nishita Kadiya

        # Task 4 : Weather App

# Importing Necessary Libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk    # interactive user interface
import requests # for getting data from weather api
from PIL import ImageTk,Image
import time


# Function to get weather data from Open Weather api
def  weather_data(city_name1):

    API_KEY1 = "8e44a61cc2a8f4eaf0c599737ca7a49d"
    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name1}&appid={API_KEY1}"

    # making request to open weather api throungh url
    req = requests.get(url1)

    # error handling if city is not found
    if req.status_code == 404:
        print("City not found,.....")
        return None
    
    # otherwise getting the weather information from open weather api
    weather = req.json()

    get_image1 = weather['weather'][0]['icon']
    get_temp1 = weather['main']['temp'] - 273.15
    min_temp1= weather['main']['temp_min'] - 273.15
    max_temp1 = weather['main']['temp_max'] - 273.15
    get_dec1 = weather['weather'][0]['description']
    get_humidity1 = weather['main']['humidity']
    get_wind1 = weather['wind']['speed']
    get_sunrise1 = time.strftime("%I:%M:%S", time.gmtime(weather['sys']['sunrise'] - 21600))
    get_sunset1 = time.strftime("%I:%M:%S", time.gmtime(weather['sys']['sunset'] - 21600))
    print(get_sunrise1)
    city_name1 = weather['name']
    coun1 = weather['sys']['country']
    
    print(min_temp1)
    icon_url = f"https://openweathermap.org/img/wn/{get_image1}@2x.png"

    return(icon_url,get_image1,get_temp1,get_dec1,get_humidity1,get_wind1,city_name1,coun1,min_temp1,max_temp1,get_sunrise1,get_sunset1)

# function to display weather information in associated label
def set_info():

    city_name1 = city_in.get()  

    # calling weather_data function to fetch the weather info 
    info = weather_data(city_name1)
    icon_url,get_image1,get_temp1,get_desc1,get_humidity1,get_wind1,city_name1,coun1,min_temp1,max_temp1,get_sunrise1,get_sunset1 = info
    location_label.config(text=f"{city_name1},  {coun1}")

    if info is None:
        print("no inforamtion is avaliable through API")
        return
    
    # otherwise setting info
    image = requests.get(icon_url, stream=True)
    display_image = Image.open(image.raw)
    set_image = ImageTk.PhotoImage(display_image)
    image_label.config(image=set_image,background="lightslategrey")
    image_label.image = set_image

    sunrise_label.config(text=f"Sunrise : {get_sunrise1}, Sunset : {get_sunset1}")
    temp_label.config(text=f"Temperature : {get_temp1:.2f}°C")
    temp_details.config(text=f"Minimum Temperature : {min_temp1:.2f}°C\n Maximum Temperature : {max_temp1:.2f}°C")
    desc_label.config(text=f"Description : {get_desc1}")
    humidity_label.config(text=f"Humidity : {get_humidity1}%")
    wind_label.config(text=f"Wind Speed : {get_wind1} m/s")
   
# initiaze rooot window nd its property
rooot = Tk()
rooot.title("Weather App")
rooot.geometry("500x750")
rooot.resizable(False,False)
rooot.config(bg="lightslategrey")

image_path = 'title.png'                           # Titale image 
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
t_image = tk.Label(rooot,image=photo)
t_image.image = photo
t_image.place(x=140,y=20)

# input for city or country
city_label1 = ttk.Label(rooot,text="Enter City name or Country Name",font="Times 20 bold",background="lightslategrey")
city_label1.pack(pady=150)

city_in = ttk.Entry(rooot,width=30,justify=CENTER,font="Helvetice 18 bold")
city_in.place(x=60,y=200)

Button(rooot,text="Get Weather Data",width=15,height=1,font="Times 22",bg="black",fg="white",command=set_info).place(x=130,y=400)

image_label = Label(rooot)
image_label.place(x=200,y=250)

# Displaying weather information that are fetch from open weather api
location_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
location_label.place(x=130,y=480)

sunrise_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
sunrise_label.place(x=130,y=510)

temp_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
temp_label.place(x=130,y=540)

temp_details = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
temp_details.place(x=130,y=570)

desc_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
desc_label.place(x=130,y=620)

humidity_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
humidity_label.place(x=130,y=650)

wind_label = Label(rooot,foreground="black",font="Times 16",background="lightslategrey")
wind_label.place(x=130,y=680)

rooot.mainloop()



    



    