from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime

import sqlite3

root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")



def home():
    root.destroy()
    import dashboard

def std():
    root.destroy()
    import student


def signOut():
    root.destroy()
    import login

def show_user_menu(event):
    user_menu.post(event.x_root, event.y_root)

profile_image = PhotoImage(file="b.png")

# Create a profile icon button with the image
profile_icon_button = Button(root, cursor='hand2', image=profile_image, bd=0, bg="white", width=32, height=32)
profile_icon_button.place(x=1420, y=10)

# Create a menu for the user
user_menu = Menu(root, tearoff=0, bg="lightgray", fg="black", font=("Helvetica", 10, "bold"))
user_menu.add_command(label="Sanjeev Manandhar", font=("Helvetica", 10), command=lambda: print("User clicked"))
user_menu.add_separator()
user_menu.add_command(label="Sign out", font=("Helvetica", 10, "bold"), command=signOut)

# Bind the menu to the profile icon button
profile_icon_button.bind("<Button-1>", show_user_menu)
    



big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)



home=Button(big_label,cursor='hand2',text="Home",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=home)
home.place(x=40,y=500)

student=Button(big_label,cursor='hand2',text="Student",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=std)
student.place(x=40,y=560)



invoice=Button(big_label,cursor='hand2',text="Setting",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
invoice.place(x=40,y=620)


# stering image
image = Image.open("drivelogo.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=17,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",13,"bold"),fg="white",bg="#152844")
pro.place(x=78,y=100)

def change_password():
    email = email_entry.get()
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    if new_password != confirm_password:
        messagebox.showerror("Error", "New password and confirm password do not match")
        return

    conn = sqlite3.connect('dri.db')
    cursor = conn.cursor()

    # Check if the email exists in the database
    cursor.execute("SELECT * FROM information WHERE email=?", (email,))
    user = cursor.fetchone()
    if user is None:
        messagebox.showerror("Error", "Email not found")
        conn.close()
        return

    # Convert both passwords to lowercase before comparison
    if user[5].lower() != old_password.lower():
        messagebox.showerror("Error", "Incorrect old password")
        conn.close()
        return

    # Update the password for the user
    cursor.execute("UPDATE information SET password=? WHERE email=?", (new_password, email))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Password changed successfully")

    # Clear the entry fields
    email_entry.delete(0, END)
    old_password_entry.delete(0, END)
    new_password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)




# Labels
email=Label(root, text="email").place(x=600,y=80)
email_entry = Entry(root)
email_entry.place(x=600,y=120)

old=Label(root, text="Old Password").place(x=600,y=150)
old_password_entry = Entry(root, show="*")
old_password_entry.place(x=600,y=200)

Label(root, text="New Password").place(x=600,y=250)
new_password_entry = Entry(root, show="*")
new_password_entry.place(x=600,y=300)

Label(root, text="Confirm Password").place(x=600,y=350)
confirm_password_entry = Entry(root, show="*")
confirm_password_entry.place(x=600,y=400)

# Change Password Button
Button(root, cursor='hand2', text="Change Password", command=change_password).place(x=600,y=500)
root.mainloop()