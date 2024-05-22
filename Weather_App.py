from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk 

window = Tk()
window.title("Weather app")
window.geometry("890x470+300+200")
window.config(bg="#57adff")
window.resizable(False, False)


def get_weather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geopyExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather
    api = ("https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="
           +str(location.longitude)+"&units=metric&exclude=hourly&appid=cbdac************7461f0677a4f71f")
    json_data = requests.get(api).json()

    # current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]["description"]

    #print(temp)
    #print(humidity)
    #print(pressure)
    #print(wind)
    #print(description)

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)


    # first_cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
       # print(firstdayimage)
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = json_data["daily"][0]["temp"]['day']
    tempnight1 = json_data["daily"][0]["temp"]['night']

    day1temp.config(text=f'Day:{tempday1}\n Night:{tempnight1}')
    

    # second_cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
       # print(firstdayimage)
    img = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2 = json_data["daily"][1]["temp"]['day']
    tempnight2 = json_data["daily"][1]["temp"]['night']

    day2temp.config(text=f'Day:{tempday2}\n Night:{tempnight2}')

    # third_cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
       # print(thirddayimage)
    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    tempday3 = json_data["daily"][2]["temp"]['day']
    tempnight3 = json_data["daily"][2]["temp"]['night']

    day3temp.config(text=f'Day:{tempday3}\n Night:{tempnight3}')

    # forth_cell
    forthdayimage = json_data['daily'][3]['weather'][0]['icon']
       # print(forthdayimage)
    img = (Image.open(f"icon/{forthdayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo4 = ImageTk.PhotoImage(resized_image)
    forthimage.config(image=photo4)
    forthimage.image=photo4

    tempday4 = json_data["daily"][3]["temp"]['day']
    tempnight4 = json_data["daily"][3]["temp"]['night']

    day4temp.config(text=f'Day:{tempday4}\n Night:{tempnight4}')


    # fifth_cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
      # print(fifthdayimage)
    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5 = json_data["daily"][4]["temp"]['day']
    tempnight5 = json_data["daily"][4]["temp"]['night']

    day5temp.config(text=f'Day:{tempday5}\n Night:{tempnight5}')

    # sixth_cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
      # print(sixthdayimage)
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6 = json_data["daily"][5]["temp"]['day']
    tempnight6 = json_data["daily"][5]["temp"]['night']

    day6temp.config(text=f'Day:{tempday6}\n Night:{tempnight6}')

    # seventh_cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
      # print(seventhdayimage)
    img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image=img.resize((30, 30))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7 = json_data["daily"][6]["temp"]['day']
    tempnight7 = json_data["daily"][6]["temp"]['night']

    day7temp.config(text=f'Day:{tempday7}\n Night:{tempnight7}')

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    forth = first+timedelta(days=3)
    day4.config(text=forth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

   
    

# icon


image_icon = PhotoImage(file="Images/icon.png")
window.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(window, image=Round_box, bg="#57adff").place(x=30, y=110)

# Label
label1 = Label(window, text="Temperature", font=("Helvetica", 10), fg="white", bg="#3c3c3c")
label1.place(x=50, y=120)

label2 = Label(window, text="Humidity", font=("Helvetica", 10), fg="white", bg="#3c3c3c")
label2.place(x=50, y=140)

label3 = Label(window, text="Pressure", font=("Helvetica", 10), fg="white", bg="#3c3c3c")
label3.place(x=50, y=160)

label4 = Label(window, text="Wind speed", font=("Helvetica", 10), fg="white", bg="#3c3c3c")
label4.place(x=50, y=180)

label5 = Label(window, text="Description", font=("Helvetica", 10), fg="white", bg="#3c3c3c")
label5.place(x=50, y=200)

# SEARCH BOX
search_image = PhotoImage(file="Images/Search.png")
myImage = Label(window, image=search_image, bg="#57adff")
myImage.place(x=270, y=120)

weather_Image = PhotoImage(file="Images/Layer 7.png")
weather_image = Label(window, image=weather_Image, bg="#203243")
weather_image.place(x=295, y=127)

textfield = tk.Entry(window, justify="center", width=15, font=("poppins", 25, "bold"), bg="#203243", border=0,
                     fg="#fff")
textfield.place(x=350, y=130)
textfield.focus()

search_icon = PhotoImage(file="Images/searchicon.png")
my_image_icon = Button(window, image=search_icon, bg="#203243", cursor="hand2", command=get_weather)
my_image_icon.place(x=570, y=130)

# Bottom Box
frame = Frame(window, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom Boxes
firstBox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondBox = PhotoImage(file="Images/copy.png")

Label(frame, image=firstBox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=300, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=400, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=500, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=600, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=700, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=800, y=20)

# clock (here we will place time)
clock = Label(window, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# timezone
timezone = Label(window, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(window, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)


# thpwd
t = Label(window, font=("Helvetica", 11), fg="white", bg="#3c3c3c")
t.place(x=135, y=120)
h = Label(window, font=("Helvetica", 11), fg="white", bg="#3c3c3c")
h.place(x=135, y=140)
p = Label(window, font=("Helvetica", 11), fg="white", bg="#3c3c3c")
p.place(x=135, y=160)
w = Label(window, font=("Helvetica", 11), fg="white", bg="#3c3c3c")
w.place(x=135, y=180)
d = Label(window, font=("Helvetica", 11), fg="white", bg="#3c3c3c")
d.place(x=135, y=200)

# first_cell
first_frame = Frame(window, width=185, height=113, bg="#282829")
first_frame.place(x=38, y=315)

day1 = Label(first_frame, font="arial 20", bg="#282829", fg="white")
day1.place(x=70, y=5)

firstimage = Label(first_frame, bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(first_frame,bg="#282829",fg="#57adff", font="arial 15 bold")
day1temp.place(x=60, y=50)

# second_cell
second_frame = Frame(window, width=63, height=90, bg="#282829")
second_frame.place(x=305, y=320)

day2 = Label(second_frame, bg="#282829", fg="white")
day2.place(x=10, y=5)

secondimage = Label(second_frame, bg="#282829")
secondimage.place(x=7,y=20)

day2temp=Label(second_frame,bg="#282829",fg="#fff")
day2temp.place(x=1, y=50)

# third_cell
third_frame = Frame(window, width=63, height=90, bg="#282829")
third_frame.place(x=405, y=320)

day3 = Label(third_frame, bg="#282829", fg="white")
day3.place(x=5, y=5)

thirdimage = Label(third_frame, bg="#282829")
thirdimage.place(x=7,y=20)

day3temp=Label(third_frame,bg="#282829",fg="#fff")
day3temp.place(x=1, y=50)

# forth_cell
forth_frame = Frame(window, width=63, height=90, bg="#282829")
forth_frame.place(x=505, y=320)

day4 = Label(forth_frame, bg="#282829", fg="white")
day4.place(x=10, y=5)

forthimage = Label(forth_frame, bg="#282829")
forthimage.place(x=7,y=20)

day4temp=Label(forth_frame,bg="#282829",fg="#fff")
day4temp.place(x=1, y=50)

# fifth_cell
fifth_frame = Frame(window, width=63, height=90, bg="#282829")
fifth_frame.place(x=605, y=320)

day5 = Label(fifth_frame, bg="#282829", fg="white")
day5.place(x=10, y=5)

fifthimage = Label(fifth_frame, bg="#282829")
fifthimage.place(x=7,y=20)

day5temp=Label(fifth_frame,bg="#282829",fg="#fff")
day5temp.place(x=1, y=50)

# sixth_cell
sixth_frame = Frame(window, width=63, height=90, bg="#282829")
sixth_frame.place(x=705, y=320)

day6 = Label(sixth_frame, bg="#282829", fg="white")
day6.place(x=10, y=5)

sixthimage = Label(sixth_frame, bg="#282829")
sixthimage.place(x=7,y=20)

day6temp=Label(sixth_frame,bg="#282829",fg="#fff")
day6temp.place(x=1, y=50) # x=10



# seventh_cell
seventh_frame = Frame(window, width=63, height=90, bg="#282829") # bg="#282829
seventh_frame.place(x=805, y=320)

day7 = Label(seventh_frame, bg="#282829", fg="white")
day7.place(x=10, y=5)

seventhimage = Label(seventh_frame, bg="#282829")
seventhimage.place(x=7,y=20)

day7temp=Label(seventh_frame,bg="#282829",fg="#fff")
day7temp.place(x=1, y=50)


window.mainloop()
