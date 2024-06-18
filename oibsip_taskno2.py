# NISHITA KADIYA 

        # TASK 2 : BMI Calculator

# Requiremnets :
#pip install pillow
#Formula : kg / m**2

# Importing Necessary libraries 
from tkinter import *           # for graphical user Interface
import tkinter as tk            # initiaze tkinter as tk so that we dont have to write its full name
from tkinter import ttk
from PIL import Image,ImageTk  # from pillow we are importing image to make it interactive

# initiaze window rooot and its title, initial size and background color
rooot = Tk()
rooot.title("BMI Calculator")
rooot.geometry("500x630")
rooot.resizable(False,False)
rooot.configure(bg="#dddddd")

# main formula applied here for the calculation
def Cal():
    height = float(height_in.get())
    weight = float(weight_in.get())

    # convertingg h to m
    meter = height/100
    ans = round(float(weight/meter**2),1)
    print(ans)
    score.config(text=f"Your Score : {ans}")

    # conditions for output
    if ans<=18.5:
        op.config(text="Under Weight..",fg="blue")  # 165,43.5
        summary1.config(text="Your Weight and height fall below \n the average range for your body type!")

    elif ans>18.5 and ans<=25:
        op.config(text="Normal !!",fg="green")  # 173.9, 71.63
        summary1.config(text="Congratulations!! \n You are Healthy!")

    elif ans>25 and ans<=30: # 185,97
        op.config(text="Over Weight !!",fg="orange")
        summary1.config(text="Oops, You Are Slightly Over Weight ! \n Get an advice from doctor")
    
    else:  # 140.7, 104.8
        op.config(text="Worried !!",fg="red")
        summary1.config(text="You are more then overweight! \n Your Health is at Risk.")

# setting BMI Icon image at title bar
bmi_icon = PhotoImage(file='icon.png')
rooot.iconphoto(False,bmi_icon)

# setting The Titale content
title_frame = tk.Frame(rooot)
title_frame.pack(fill="x",pady=50)

title = tk.Label(title_frame,text="BMI Calculator",font=("Times New Roman",24),foreground="dark blue")
title.pack(side="left",padx=150)

# setting bottom base for scaling and calculating
b = Label(rooot,width=70,bg="#F5F5DC",height=20)
b.pack(side=BOTTOM)

# making box for user input weight and height
inputs = PhotoImage(file='box.png')
l1 = Label(rooot,image=inputs)
l1.place(x=20,y=100)
l2 = Label(rooot,image=inputs)
l2.place(x=240,y=100)

# making slider for weight so user can move value
val1 = tk.DoubleVar()

# this function gets the value of height
def got_val1():
    return val1.get()

# used to change value by slider
def slide1(event):
    height_in.set(got_val1())
    update_user()  # updating user position for visualization
    
slide1 = ttk.Scale(rooot,from_=0, to=220, command=slide1,variable=val1,orient='horizontal')
slide1.place(x=80,y=250)

# making slider for height
val2 = tk.DoubleVar()

def got_val2():  # gets the value of weight
    return val2.get()

def slide2(event):
    weight_in.set(got_val2())
    update_user()  # changing position of weight

slide2 = ttk.Scale(rooot,from_=0,to=220,command=slide2,variable=val2,orient='horizontal')
slide2.place(x=300,y=250)

# updating user icon bsed on height and weight
def update_user():
    h1 = int(float(height_in.get()))
    w1 = int(float(weight_in.get()))
    user1 = Image.open('user.png')
    user_resize = user1.resize((50+w1, 10+h1))
    p2 = ImageTk.PhotoImage(user_resize)
    user.config(image=p2)
    user.place(x=70,y=590-h1)
    user.image = p2


# taking inputs from user
a = Label(rooot,text="Height",font="arial 18",justify=CENTER,foreground="black")
a.place(x=90,y=120)
height_in = StringVar()
weight_in = StringVar()
h1 = Entry(rooot,width=5,justify=CENTER,bg="white",bd=1,fg="black",font="arial 30",textvariable = height_in)
h1.place(x=80,y=160)
height_in.set(got_val1())

# taking weight input

b = Label(rooot,text="Weight",font="arial 18",justify=CENTER,foreground="black")
b.place(x=300,y=120)
w1 = Entry(rooot,width=5,justify=CENTER,bg="white",bd=1,fg="black",font="arial 30",textvariable=weight_in)
w1.place(x=290,y=160)
weight_in.set(got_val2())

# user image setting
user = Label(rooot,bg="#F5F5DC")
user.place(x=70,y=530)

# setting for scale image so than user can move up and down the values of weight and height
line = PhotoImage(file='scale.png')
c = Label(rooot,image=line,bg="#F5F5DC")
c.place(x=20,y=350)

# Final Calculating button and gives command to calculation
x = Button(rooot,text="Calculate BMI",command=Cal,bg="black",foreground="white",width=15,font="arial 12 bold",height=2)
x.place(x=280,y=350)

score = Label(rooot,font="arial 28 bold",bg="#F5F5DC",fg="black")
score.place(x=155,y=420)

# final output
op = Label(rooot,font="arial 22 bold",bg="#F5F5Dc",fg="red")
op.place(x=215,y=480)

# 1 line note according to op
summary1 = Label(rooot,font="arial 16",bg="#F5F5DC",fg="black")
summary1.place(x=155,y=530)

rooot.mainloop()