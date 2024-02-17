

from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3



root= Tk()

#Start login page
root.title("login")

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required.')
    else:
        conn = sqlite3.connect("dri.db")
        db = conn.cursor()
        
        email = username_entry.get()
        password = password_entry.get()
        
        db.execute("SELECT * FROM information WHERE email=? AND password=?", (email, password))

        user_data = db.fetchone()
        
        if user_data==None:
            messagebox.showerror('Error','Invalid username or password.')  
        else:
            messagebox.showinfo('Welcome','Login is Successful.')
           
            
        conn.close()

def forget_password():
    window=Toplevel()
    window.config(bg='black')
    window.title('password change.')
    window.geometry(f'370x400+561+195')
    heading_label=Label(window,bg='black', text='Reset Password',font=('cabiler',18,'bold'),fg='#66a3ff')
    heading_label.place(x=80,y=20)
    email=Label(window,text="Email",bg='black',font=('cabiler',12,'bold'),fg='sky blue')
    email.place(x=30,y=80)
    email_entry=Entry(window,width=25,fg='white',bg='black',font=("cabiler", 10, "bold"),bd=0)
    email_entry.place(x=30,y=110)
    Frame(window,width=270,height=2,bg='white').place(x=30,y=130)

    new_pass=Label(window,text="New Password",bg='black',font=('cabiler',12,'bold'),fg='sky blue')
    new_pass.place(x=30,y=150)
    new_pass_entry=Entry(window,width=25,fg='white',bg='black',font=("cabiler", 10, "bold"),bd=0)
    new_pass_entry.place(x=30,y=180)
    Frame(window,width=270,height=2,bg='white').place(x=30,y=200)

    conf_pass=Label(window,text="Confirm Password",bg='black',font=('cabiler',12,'bold'),fg='sky blue')
    conf_pass.place(x=30,y=220)
    conf_pass_entry=Entry(window,width=25,fg='white',bg='black',font=("cabiler", 10, "bold"),bd=0)
    conf_pass_entry.place(x=30,y=250)
    Frame(window,width=270,height=2,bg='white').place(x=30,y=270)
    
    submit_button=Button(window,text='Change Password',bd=0,bg='sky blue',fg='white',font=("cabiler", 16, "bold"),width=19,cursor='hand2',activebackground='black',activeforeground='sky blue')
    submit_button.place(x=55,y=320)
    
    
    window.mainloop()
          


def login():
    root.destroy()
    import signup

root.geometry("1980x1080")
welcome = Label(root, text="Welcome  to  the  entrance", font=("Cabiler", 23)).place(x=560, y=250)
login_in = Label(root, text="log into continue.", font=("Cabiler", 23)).place(x=560, y=290)
question = Label(root, text="Don't you have an account?", font=("Cabiler", 13)).place(x=560, y=350)
sign_up = Button(root, text="Create a new account.", border=0, font=("Cabiler", 13, "underline"), fg="sky blue", command=login).place(x=765, y=347)

username = Label(root, text="Email", font=("Cabiler", 10)).place(x=560, y=395)
username_entry = Entry(root, width=52, border=4, font=("cabiler", 10, "bold"))
username_entry.place(x=560, y=425, height=35)

password = Label(root, text="Password", font=("Cabiler", 10)).place(x=560, y=460)
password_entry = Entry(root, width=52, border=4, font=("cabiler", 10, "bold"), show='*')
password_entry.place(x=560, y=485, height=35)

title = Button(root,text="Forget password",border=0, font=("Cabiler",10,"underline"),fg='sky blue',command=forget_password).place(x=830, y=525)

log_in_button = Button(root, text="Log in", width=45, fg="white", bg="sky blue", font=("Caliber", 10), command=login_user)
log_in_button.place(x=560, y=565)

root.mainloop()

