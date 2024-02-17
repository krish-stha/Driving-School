

from tkinter import*
from PIL import Image, ImageTk



root= Tk()

#Start login page
root.title("login")

def login():
    root.destroy()
    import signup
    
   
    
   
    

    
   

    
   

   


root.geometry("1980x1080")
welcome = Label(root,text="Welcome  to  the  entrance",font=("Cabiler",23)).place(x=560, y=250)
login_in = Label(root,text="log into continue.",font=("Cabiler",23)).place(x=560, y=290)
question = Label(root,text="Don't you have an account?",font=("Cabiler",13)).place(x=560, y=350)
sign_up = Button(root,text="Create a new account.", border=0,font=("Cabiler",13,"underline"), fg="sky blue",command=login).place(x=765, y=347)

username = Label(root,text="Email",font=("Cabiler",10)).place(x=560, y=395)
username_entry = Entry(root,width=52,border=4,font=("cabiler",10,"bold")).place(x=560, y=425,height=35)

password = Label(root,text="Password",font=("Cabiler",10)).place(x=560, y=460)
password_entry= Entry(root,width=52,border=4,font=("cabiler",10,"bold"),show='*').place(x=560, y=485,height=35)


title = Button(root, text="Log in",width=45,fg="white", bg="sky blue", font=("Caliber",10)).place(x=560, y=555)







root.mainloop()
#login frontend end



# conn = sqlite3.connect("kri.db")
# db = conn.cursor()
# db.execute("""CREATE TABLE IF NOT EXISTS information
#                (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 address TEXT,
#                 contact INT)""")
# conn.close()