from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


root=Tk()
root.title("Sign up")
root.geometry("1920x1080")




def log_in():
    root.destroy()
    import login


def connect_database():
    conn = sqlite3.connect("dri.db")
    db = conn.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS information
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR(255),
                    firstname VARCHAR(255),
                    lastname VARCHAR(255),
                    contact INTEGER,
                    password VARCHAR(255)
                    )""")

    # Check if the email already exists
    email = email_entry.get()
    db.execute("SELECT * FROM information WHERE email=?", (email,))
    existing_user = db.fetchone()
    if existing_user:
        messagebox.showerror('Error', 'Email already exists. Please use a different email.')
    else:
        if (email_entry.get() == '' or Firstname_entry.get() == '' or Lastname_entry.get() == '' or contact_entry.get() == '' or password_entry.get() == '' or conf_password_entry.get() == ''):
            messagebox.showerror('Error', 'All Fields Are Required.')
        elif password_entry.get() != conf_password_entry.get():
            messagebox.showerror('Error', 'Password Mismatch')
        elif not email_entry.get().endswith('@gmail.com'):
            messagebox.showerror('Error', 'Email must end with "@gmail.com"')
        elif not contact_entry.get().isdigit() or len(contact_entry.get()) != 10:
            messagebox.showerror('Error', 'Contact number must be a 10-digit integer')
        elif not Firstname_entry.get().isalpha(): 
            messagebox.showerror('Error', 'First name  must be alphabets.')
        elif not Lastname_entry.get().isalpha():
            messagebox.showerror('Error', 'last name must be alphabets.')
        else:
            # Insert new user if all validations pass
            firstname = Firstname_entry.get()
            lastname = Lastname_entry.get()
            contact = contact_entry.get()
            password = password_entry.get()
            db.execute("INSERT INTO information (email, firstname, lastname, contact, password) VALUES (?, ?, ?, ?, ?)", (email, firstname, lastname, contact, password))
            
            conn.commit()  
            conn.close()   

            messagebox.showinfo('Success', 'Registration Successful')
              # Clear the form entries before destroying the window
            root.destroy()  # Destroy the window after successful registration
            import login  # Import the login module after destroying the window
            clear()



       

def clear():
    email_entry.delete(0, 'end')
    Firstname_entry.delete(0, 'end')
    Lastname_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    conf_password_entry.delete(0, 'end')


        
        

        
       
        
            

        # conn.close()
        # messagebox.showinfo('Success', 'Registration Successful')









title = Label(root,text="Already have an account?",font=("Honk",11)).place(x=1280, y=25)
Login = Button(root,text="Login",border=0,font=("Honk",11,"underline"),fg="sky blue",command=log_in).place(x=1450, y=24)


sign_up_title = Label(root,text="Sign up",font=("Cabiler",23)).place(x=1115 , y=114)
account_title = Label(root,text="Create your account",font=("cabiler",13)).place(x=1095 , y=165)

email = Label(root,text="Email*",font=("Honk",10)).place(x=1000, y=190)
email_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
email_entry.place(x=1000 , y=210,height=25)
FirstName = Label(root, text="FirstName*",font=("Honk",10)).place(x=1000, y=250)
Firstname_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
Firstname_entry.place(x=1000 , y=270,height=25)
LastName = Label(root,text="LastName*",font=("Honk",10)).place(x=1000, y=310)
Lastname_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
Lastname_entry.place(x=1000, y=330,height=25)
contact = Label(root,text="Contact No*",font=("Honk",10)).place(x=1000, y=370)
contact_entry = Entry(root,width=52,font=("cabiler",10,"bold"))
contact_entry.place(x=1000,y=390,height=25)
Password = Label(root,text="Password*",font=("Honk",10)).place(x=1000, y=430)
password_entry = Entry(root,width=52,show='*',font=("cabiler",10,"bold"))
password_entry.place(x=1000, y=450,height=25)
conf_Password = Label(root,text="Confirm Password*",font=("Honk",10)).place(x=1000, y=490)
conf_password_entry = Entry(root,width=52,show='*',font=("cabiler",10,"bold"))
conf_password_entry.place(x=1000, y=510,height=25)
Register_button = Button(root,text="Register",width=45,border=0,fg="white",bg="sky blue", font=("Honk",10),command=connect_database).place(x=1000, y=560,height=28)
image = Image.open("loginnn.jpg")  
photo = ImageTk.PhotoImage(image)

image_label=Label(root,bg="grey",width=782,height=789,image=photo)
image_label.place(x=0)

root.mainloop()
