from tkinter import*
from PIL import Image, ImageTk

def log_in():
    import login
    root.destroy()



root=Tk()
root.title("Sign up")

root.geometry("1920x1080")

title = Label(root,text="Already have an account?",font=("Honk",11)).place(x=1280, y=25)
Login = Button(root,text="Login",border=0,font=("Honk",11,"underline"),fg="sky blue",command=log_in).place(x=1450, y=24)

sign_up_title = Label(root,text="Sign up",font=("Cabiler",23)).place(x=1115 , y=114)
account_title = Label(root,text="Create your account",font=("cabiler",13)).place(x=1095 , y=165)

email = Label(root,text="Email*",font=("Honk",10)).place(x=1000, y=190)
email_entry = Entry(root,width=52,font=("cabiler",10,"bold")).place(x=1000 , y=210,height=25)
FirstName = Label(root, text="FirstName*",font=("Honk",10)).place(x=1000, y=250)
Firstname_entry = Entry(root,width=52,font=("cabiler",10,"bold")).place(x=1000 , y=270,height=25)
LastName = Label(root,text="LastName*",font=("Honk",10)).place(x=1000, y=310)
Lastname_entry = Entry(root,width=52,font=("cabiler",10,"bold")).place(x=1000, y=330,height=25)
contact = Label(root,text="Contact No*",font=("Honk",10)).place(x=1000, y=370)
contact_entry = Entry(root,width=52,font=("cabiler",10,"bold")).place(x=1000,y=390,height=25)
Password = Label(root,text="Password*",font=("Honk",10)).place(x=1000, y=430)
password_entry = Entry(root,width=52,show='*',font=("cabiler",10,"bold")).place(x=1000, y=450,height=25)

Register_button = Button(root,text="Register",width=45,border=0,fg="white",bg="sky blue", font=("Honk",10)).place(x=1000, y=500,height=28)


image = Image.open("loginn.jpg")  
photo = ImageTk.PhotoImage(image)

image_label=Label(root,bg="grey",width=782,height=789,image=photo)
image_label.place(x=0)


root.mainloop()