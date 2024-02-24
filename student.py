from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

import sqlite3

def add_student_record(first_name, last_name, dob, client_id, email, phone, street, city, state, zip_code, country):
    # Connect to the database
    conn = sqlite3.connect("dri.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        dob TEXT,
                        client_id TEXT,
                        email TEXT,
                        phone TEXT,
                        street TEXT,
                        city TEXT,
                        state TEXT,
                        zip TEXT,
                        country TEXT
                    )''')

    # Insert data into the database
    cursor.execute('''INSERT INTO students (first_name, last_name, dob, client_id, email, phone, street, city, state, zip, country) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (first_name, last_name, dob, client_id, email, phone, street, city, state, zip_code, country))

    # Commit changes and close connection
    conn.commit()
    conn.close()



def home():
    root.destroy()
    import dashboard
    
root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")
image1 = Image.open("b.png")  
photo1 = ImageTk.PhotoImage(image1)

image_label=Button(root,image=photo1,bd=0,bg="white")
image_label.place(x=1420,y=10)




image2 = Image.open("real.png") 
photo2 = ImageTk.PhotoImage(image2)

search_button = Button(root, image=photo2,bg="white",bd=0,height=35,activebackground="white")
search_button.place(x=525, y=15)

big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)

placeholder = "Search Contacts"


entry =Entry( root,width=15, font=("cabiler", 14,"bold"),fg="black",bd=0)  

entry.insert(0, placeholder)
entry.bind("<FocusIn>", lambda event: entry.delete(0, END) if entry.get() == placeholder else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if entry.get() == "" else None)
entry.config(fg='grey')  


entry.place(x=370,y=22)



#LEFT LABEL

home=Button(big_label,text="Home",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=home)
home.place(x=40,y=500)

student=Button(big_label,text="Student",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
student.place(x=40,y=560)


invoice=Button(big_label,text="Invoice",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
invoice.place(x=40,y=620)





# stering image
image = Image.open("drivelogo.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=0,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",16),fg="white",bg="#152844")
pro.place(x=100,y=120)








# image_button.place(x=505, y=35)



root.mainloop()

