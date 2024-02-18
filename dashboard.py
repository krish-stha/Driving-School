from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")


# add button
def form():
    window=Toplevel()
    window.config()
    window.title('Details')
    window.geometry(f'900x400+450+195')

    def add():
        messagebox.showinfo("Success","Added  Successfully")

        window.destroy()


    
    # Personal details 
    personal = Label(window,text="PERSONAL DETAILS",border=5,font=("arial rounded MT Bold",10,"bold"),fg="#3985FF").place(x=10, y=10)
    first_name = Label(window,text="First Name",font=("arial rounded MT Bold",8)).place(x=10, y=50)
    first_name_box = Entry(window,width=40).place(x=10, y=70)
    last_name = Label(window,text="Last Name",font=("arial rounded MT Bold",8)).place(x=300, y=50)
    last_name_box = Entry(window,width=40).place(x=300, y=70)
    date = Label(window,text="D.O.B",font=("arial rounded MT Bold",8)).place(x=10, y=100)
    date_box = Entry(window, width=40).place(x=10, y=120)
    instruction = Label(window,text="Date must be in YYYY-MM-DD[2012-12-22]format",font=("arial rounded MT Bold",7)).place(x=10, y=140)
    Client_id = Label(window,text="Client id",font=("arial rounded MT Bold",8)).place(x=300, y=100)
    client_id_box = Entry(window,width=40).place(x=300, y=120)

    email = Label(window,text="Email",font=("arial rounded MT Bold",8)).place(x=600,y=50)
    email_box = Entry(window,width=40).place(x=600, y=70)
    phone = Label(window,text="Phone",font=("arial rounded MT Bold",8)).place(x=600,y=100)
    phone_box = Entry(window,width=40).place(x=600, y=120)


    street = Label(window,text="Street",font=("arial rounded MT Bold",8)).place(x=10,y=180)
    street_box = Entry(window,width=40).place(x=10, y=200)
    city = Label(window,text="City",font=("arial rounded MT Bold",8)).place(x=300,y=180)
    city_box = Entry(window,width=40).place(x=300, y=200)
    state = Label(window,text="State",font=("arial rounded MT Bold",8)).place(x=600,y=180)
    state_box = Entry(window,width=40).place(x=600, y=200)

    zip = Label(window,text="Zip/Post Code",font=("arial rounded MT Bold",8)).place(x=10,y=250)
    zip_box = Entry(window,width=40).place(x=10, y=270)
    country = Label(window,text="Country",font=("arial rounded MT Bold",8)).place(x=300,y=250)
    country_box = Entry(window,width=40).place(x=300, y=270)

    add_button=Button(window,text="Add",font=("arial rounded MT Bold",12,"bold"),height=2,width=15,activebackground="#3985FF",bg="#3985FF",fg="white",command=add)
    add_button.place(x=350,y=320)

    root.mainloop()


# document section
    



    
   


# root element

image1 = Image.open("b.png")  
photo1 = ImageTk.PhotoImage(image1)

image_label=Button(root,image=photo1,bd=0,bg="white")
image_label.place(x=1420,y=10)


add_student=Button(root,text="Add Student",bg="#3985FF",fg="white",height=2,width=15,activebackground="#3985FF",command=form)
add_student.place(x=370,y=15)

image2 = Image.open("real.png")  
photo2 = ImageTk.PhotoImage(image2)

search_button = Button(root, image=photo2,bg="white",bd=0,height=35)
search_button.place(x=487, y=15)

big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)

placeholder = "Search Contacts"


entry =Entry( root,width=25, font=("cabiler", 14,"bold"),fg="black",bd=0)  

entry.insert(0, placeholder)
entry.bind("<FocusIn>", lambda event: entry.delete(0, END) if entry.get() == placeholder else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if entry.get() == "" else None)
entry.config(fg='grey')  # Change text color to grey


entry.place(x=535,y=22)



#LEFT LABEL

home=Button(big_label,text="Home",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
home.place(x=40,y=500)

student=Button(big_label,text="Student",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
student.place(x=40,y=560)


invoice=Button(big_label,text="Invoice",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
invoice.place(x=40,y=620)



##### 3 box

inquiry=Label(right_label, height=20, width=45, relief="sunken",bg="white",bd=3)
inquiry.place(x=50, y=220)

inquiry_text=Label(right_label, height=5, width=46,text="Number Of Inquiry",fg="white",font=("arial rounded MT Bold",8), relief="ridge",bg="#3985FF")
inquiry_text.place(x=50, y=520)

ongoing=Label(right_label, height=20, width=45, bg="white",relief="sunken", bd=3)
ongoing.place(x=430, y=220)

ongoing_text=Label(right_label, height=5, text="Number Of Ongoing Student",fg="white",font=("arial rounded MT Bold",8),width=46, bg="#3985FF", bd=1, relief="ridge")
ongoing_text.place(x=430, y=520)

closed=Label(right_label, height=20, width=45,bg="white",relief="sunken", bd=3)
closed.place(x=800, y=220)

closed_text=Label(right_label, height=5,text="Number Of Closed Student",fg="white",font=("arial rounded MT Bold",8), width=46, bg="#3985FF", bd=1, relief="ridge")
closed_text.place(x=800, y=520)

# stering image
image = Image.open("g.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=0,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",16),fg="white",bg="#152844")
pro.place(x=100,y=120)








# image_button.place(x=505, y=35)



root.mainloop()
