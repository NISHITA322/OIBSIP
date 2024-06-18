# NISHITA KADIYA

                    # TASK 3 : Password Generator

# Importing necessary libraries
import tkinter as tk                        # For user interface
import random                               # generated password randomly based on letters, digits, symbols
import string                               # used to get all the values of letters, digits, symbols
from tkinter import *
from tkinter import ttk
from tkinter import messagebox              # showing success or failure message
import pyperclip                            # to copy the password

# function that generates password
def make_pwd1():
    
    try:
        pwd_len = int(len_input.get())

        # making condition, so if the vaule is 0 or -1, then error can be handled at runtime
        if pwd_len <= 0:
            messagebox.showerror("Invalid Input","Password length should be greater then 1")

        else:

            ans = ""

            # getting all the values of letters, digits, symbols
            ans = string.ascii_letters + string.digits + string.punctuation

            # out of all values, select some values randomly
            password = ''.join(random.choice(ans) for _ in range(pwd_len))
            print(password)

            messagebox.showinfo("Success","Your Password Generated Successfully!! \nClick on copy button to use it anywhere..")

            password_ans.config(text=password)

                #  enable the copy btn after successfully generate password
            co_btn.config(state=tk.NORMAL)
    
    except:
        pass

# funtions that gets the value of generated password and then copy it, so that user can paste it anywhere
def copypwd1():

    pwd = password_ans.cget("text")
    pyperclip.copy(pwd)
    messagebox.showinfo("Success","Your Password copied Successfully!! \n You can paste it anywhere")

# defining window
rooot = Tk()
rooot.title("Password Generator")
rooot.geometry("550x650")
rooot.resizable(False,False)
rooot.config(bg="#1D2856")  #B2ABCD

title_name = ttk.Label(rooot,text="PASSWORD GENERATOR",font=('Arial 24 bold'),foreground="#FFFFFF",background="#1D2856")
title_name.place(x=100,y=50)

# Label for password length
pwdlen_label = Label(rooot,text="Enter the Length of Password ",font=("Times 20"),foreground="#E76A35",background="#1D2856")
pwdlen_label.place(x=60,y=150)

# user input for length
len_input = tk.Entry(rooot,width=10,justify=CENTER,font=("Times",18))
len_input.place(x=400,y=150)

pwd_btn = tk.Button(rooot,text="Create Password",font=("Times 22 bold"),justify=CENTER,command=make_pwd1,bg="#FFB6C1")
pwd_btn.place(x=180,y=250)

op_label = tk.Label(rooot,text="Generated Password",font=("Times 22 bold"),bg="#1D2856",foreground="white")
op_label.place(x=160,y=380)

password_ans = tk.Label(rooot,width=30,font="Times 18",background="lightgrey",foreground="black")
password_ans.place(x=80,y=420)

co_btn = tk.Button(rooot,text="Copy Password",font=("Times 18 bold"),command=copypwd1,state=tk.DISABLED,bg="#FFB6C1")
co_btn.place(x=200,y=490)

rooot.mainloop()









