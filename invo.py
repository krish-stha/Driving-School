from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime

root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")

def home():
    """
    Closes the current window and navigates to the dashboard.

    This function closes the current Tkinter window (root) and then imports
    the dashboard module to navigate to the dashboard page.

    Returns:
        None
    """
    root.destroy()
    import dashboard

def std():
    """
    Closes the current window and navigates to the student page.

    This function closes the current Tkinter window (root) and then imports
    the student module to navigate to the student page.

    Returns:
        None
    """
    root.destroy()
    import student

def signOut():
    """
    Closes the current window and navigates to the login page.

    This function closes the current Tkinter window (root) and then imports
    the login module to navigate to the login page.

    Returns:
        None
    """
    root.destroy()
    import login

def show_user_menu(event):
    """
    Displays the user menu at the specified coordinates.

    This function displays the user menu at the specified coordinates (event.x_root, event.y_root).

    Args:
        event (Tkinter.Event): The event that triggered the menu display.

    Returns:
        None
    """
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
    """
    Changes the password for the user.

    This function gets the email, old password, new password, and confirm password from the entry fields,
    validates the input, including ensuring that the new password matches the confirm password,
    checks if the email exists in the database, verifies the old password, updates the password in the database,
    and shows a success message. If any validation fails, it displays an error message.

    Returns:
        None
    """
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

invo_label=Label(root,bg="white",relief="ridge",bd=2)  
invo_label.place(x=700,y=80,height=660,width=500) 

heading_label=Label(invo_label,bg='white', text='Change Password',font=('cabiler',18,'bold'),fg='black')
heading_label.place(x=100,y=20)

email=Label(invo_label,text="Email",bg='white',font=('cabiler',12,'bold'),fg='sky blue')
email.place(x=30,y=80)

email_entry=Entry(invo_label,width=40,fg='black',bg='white',font=("cabiler", 10, "bold"),bd=0)
email_entry.place(x=40,y=120)

Frame(invo_label,width=290,height=2,bg='black').place(x=30,y=140)  #####horizontal line to entry

old_pass=Label(invo_label,text="Old Password",bg='white',font=('cabiler',12,'bold'),fg='sky blue')
old_pass.place(x=30,y=170)

old_password_entry=Entry(invo_label,width=25,fg='black',bg='white',font=("cabiler", 10, "bold"),bd=0 ,show='*')
old_password_entry.place(x=40,y=210)
    
Frame(invo_label,width=290,height=2,bg='black').place(x=30,y=230)#####horizontal line to entry

new_pass=Label(invo_label,text="New Password",bg='white',font=('cabiler',12,'bold'),fg='sky blue')
new_pass.place(x=30,y=280)

new_password_entry=Entry(invo_label,width=25,fg='black',bg='white',font=("cabiler", 10, "bold"),bd=0, show='*')
new_password_entry.place(x=40,y=320)

Frame(invo_label,width=290,height=2,bg='black').place(x=30,y=340)#####horizontal line to entry

conf_pass=Label(invo_label,text="Confirm Password",bg='white',font=('cabiler',12,'bold'),fg='sky blue')
conf_pass.place(x=30,y=390)

confirm_password_entry=Entry(invo_label,width=25,fg='black',bg='white',font=("cabiler", 10, "bold"),bd=0, show='*')
confirm_password_entry.place(x=40,y=430)

Frame(invo_label,width=290,height=2,bg='black').place(x=30,y=450)#####horizontal line to entry
    
submit_button=Button(invo_label,text='Change Password',bd=0,bg='sky blue',fg='white',font=("cabiler", 16, "bold"),width=19,cursor='hand2',activebackground='black',activeforeground='sky blue',command=change_password)
submit_button.place(x=70,y=550)
    
root.mainloop()


################END####################