from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime

import sqlite3


def home():
    root.destroy()
    import dashboard

def std():
    root.destroy()
    import student
    
root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")
image1 = Image.open("b.png")  
photo1 = ImageTk.PhotoImage(image1)

image_label=Button(root,image=photo1,bd=0,bg="white")
image_label.place(x=1420,y=10)


big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)

image2 = Image.open("real.png") 
photo2 = ImageTk.PhotoImage(image2)

search_button = Button(root, image=photo2,bg="white",bd=0,height=35,activebackground="white")
search_button.place(x=525, y=15)

placeholder = "Search Contacts"


entry =Entry( root,width=15, font=("cabiler", 14,"bold"),fg="black",bd=0)  

entry.insert(0, placeholder)
entry.bind("<FocusIn>", lambda event: entry.delete(0, END) if entry.get() == placeholder else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if entry.get() == "" else None)
entry.config(fg='grey')  
entry.place(x=370,y=22)

home=Button(big_label,text="Home",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=home)
home.place(x=40,y=500)

student=Button(big_label,text="Student",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=std)
student.place(x=40,y=560)



invoice=Button(big_label,text="Invoice",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
invoice.place(x=40,y=620)


# stering image
image = Image.open("drivelogo.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=17,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",13,"bold"),fg="white",bg="#152844")
pro.place(x=78,y=100)

root.mainloop()