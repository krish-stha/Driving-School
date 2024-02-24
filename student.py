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
image = Image.open("g.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=0,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",16),fg="white",bg="#152844")
pro.place(x=100,y=120)


# image_button.place(x=505, y=35)


#editing records
def edit_record(event):
    item = tree.selection()[0]
    values = tree.item(item, "values")
    userId=values[0]
    print(userId)
    global editor
    editor = Tk()
    editor.title("Update Data")
    editor.geometry(f'900x400+450+195')
    editor.resizable(False, False)

    global firstName_editor
    global lastName_editor
    global dob_editor
    global email_edtior
    global number_editor
    global clientId_editor
    global street_editor
    global city_editor
    global state_edtior
    global country_editor
    global category_editor
    global zipCode_editor
    

    conn = sqlite3.connect("dri.db")
    # db = conn.cursor() firstName_editor.insert(0, values[0])
    # lastName_editor.insert(0, values[1])
    # dob_editor.insert(0, values[2])
    # email_edtior.insert(0, values[3])

    first_name = Label(editor,text="First Name",font=("arial rounded MT Bold",8)).place(x=10, y=50)
    firstName_editor = Entry(editor,width=40)
    firstName_editor.place(x=10, y=70)
    last_name = Label(editor,text="Last Name",font=("arial rounded MT Bold",8)).place(x=300, y=50)
    lastName_editor = Entry(editor,width=40)
    lastName_editor.place(x=300, y=70)
    date = Label(editor,text="D.O.B",font=("arial rounded MT Bold",8)).place(x=10, y=100)
    dob_editor = Entry(editor, width=40)
    dob_editor.place(x=10, y=120)
    instruction = Label(editor,text="Date must be in YYYY-MM-DD[2012-12-22]format",font=("arial rounded MT Bold",7)).place(x=10, y=140)
    Client_id = Label(editor,text="Client id",font=("arial rounded MT Bold",8)).place(x=300, y=100)
    clientId_editor = Entry(editor,width=40)
    clientId_editor.place(x=300, y=120)

    email = Label(editor,text="Email",font=("arial rounded MT Bold",8)).place(x=600,y=50)
    email_editor = Entry(editor,width=40)
    email_editor.place(x=600, y=70)
    phone = Label(editor,text="Phone",font=("arial rounded MT Bold",8)).place(x=600,y=100)
    number_editor = Entry(editor,width=40)
    number_editor.place(x=600, y=120)


    street = Label(editor,text="Street",font=("arial rounded MT Bold",8)).place(x=10,y=180)
    street_editor = Entry(editor,width=40)
    street_editor.place(x=10, y=200)
    city = Label(editor,text="City",font=("arial rounded MT Bold",8)).place(x=300,y=180)
    city_editor = Entry(editor,width=40)
    city_editor.place(x=300, y=200)
    state = Label(editor,text="State",font=("arial rounded MT Bold",8)).place(x=600,y=180)
    state_editor = Entry(editor,width=40)
    state_editor.place(x=600, y=200)

    zip = Label(editor,text="Zip/Post Code",font=("arial rounded MT Bold",8)).place(x=10,y=250)
    zip_editor = Entry(editor,width=40)
    zip_editor.place(x=10, y=270)
    country = Label(editor,text="Country",font=("arial rounded MT Bold",8)).place(x=300,y=250)
    country_editor = Entry(editor,width=40)
    country_editor.place(x=300, y=270)
    
    #defaultValuesOnEdit
    firstName_editor.insert(0, values[1])
    lastName_editor.insert(0, values[2])
    dob_editor.insert(0, values[3])
    clientId_editor.insert(0, values[4])
    email_editor.insert(0, values[5])
    number_editor.insert(0, values[6])
    street_editor.insert(0, values[7])
    city_editor.insert(0, values[8])
    state_editor.insert(0, values[9])
    country_editor.insert(0, values[10])
    zip_editor.insert(0, values[12])
    
    def on_select(value):
        
        global category_editor
        category_editor=value
        
    
    options = ["Bike", "Scooter", "Car"]

    selected_option = StringVar(editor)
    selected_option.set(options[0])
      
    
    category=Label(editor,text="Category",font=("arial rounded MT Bold",8)).place(x=600,y=250)

    option_menu = OptionMenu(editor, selected_option, *options, command=on_select)
    option_menu.config(highlightthickness=0, width=35,bg="white")  # Adjust desired_width as needed
    option_menu.place(x=600, y=270)


    #update function
    def update_data():
        
        


        

        # Check if any required field is empty
        if (firstName_editor.get() == '' or lastName_editor.get() == '' or clientId_editor.get() =='' or dob_editor.get() == '' or email_editor.get() == '' or number_editor.get() == '' or zip_editor.get() == '' or country_editor.get() == ''):
            messagebox.showerror('Error', 'All Fields Are Required.', parent=editor)
            return

        # Check if first name and last name contain only alphabets
        if not firstName_editor.get().isalpha() or not lastName_editor.get().isalpha():
            messagebox.showerror('Error', 'First name and last name should contain only alphabets.', parent=editor)
            return

         # Check if date is in the correct format and the person is above 16 years old


        try:
            birth_date = datetime.strptime(dob_editor.get(), '%Y-%m-%d')
        except ValueError:
            messagebox.showerror('Error', 'Date must be in YYYY-MM-DD format.', parent=editor)
            return

        # Get current date
        current_date = datetime.now()

        # Adjust current date if the birth date is in the future
        if birth_date > current_date:
            birth_date = birth_date.replace(year=birth_date.year - 100)  # Subtract 100 years

        # Calculate age
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

        # Check if age is below 16
        if age < 16:
            messagebox.showerror('Error', 'Age must be 16 years or older to be registered.', parent=editor)
            return


        # Check if email ends with '@gmail.com'
        if not email_editor.get().lower().endswith('@gmail.com'):
            messagebox.showerror('Error', 'Email must end with @gmail.com.', parent=editor)
            return

        # Check if phone number is a digit and has 10 digits
        if not number_editor.get().isdigit() or len(number_editor.get()) != 10:
            messagebox.showerror('Error', 'Phone number must be a 10-digit number.', parent=editor)
            return
        
        else:

            conn = sqlite3.connect("dri.db")
            db = conn.cursor()

            db.execute(
                """
            UPDATE usersData
            SET firstName = ?, lastName = ?, dob = ?, clientId=?, email=?, number=?, street=?, city=?, state=?, country=?, category=?, zipCode=?
            WHERE usersId = ?
            """,
                (
                    firstName_editor.get(),
                    lastName_editor.get(),
                    dob_editor.get(),
                    clientId_editor.get(),
                    email_editor.get(),
                    number_editor.get(),
                    street_editor.get(),
                    city_editor.get(),
                    state_editor.get(),
                    country_editor.get(),
                    category_editor,
                    zip_editor.get(),
                    userId,
                ),
            )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Added  Successfully")
            editor.destroy()
            for row in tree.get_children():
                tree.delete(row)
                show_data()
            

    edit_button = Button(editor, text="SAVE",width=20,command=update_data)
    edit_button.place(x=300, y=310)


#show data
def show_data():
    conn = sqlite3.connect("dri.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usersData")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()


tree = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "DOB", "Client ID", "Email", "Number", "Street", "City", "State", "Country", "Category", "Zip Code"), show="headings")
tree.place(x=370,y=120)

tree.heading("ID", text="ID")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("DOB", text="DOB")
tree.heading("Client ID", text="Client ID")
tree.heading("Email", text="Email")
tree.heading("Number", text="Number")
tree.heading("Street", text="Street")
tree.heading("City", text="City")
tree.heading("State", text="State")
tree.heading("Country", text="Country")
tree.heading("Category", text="Category")
tree.heading("Zip Code", text="Zip Code")

tree.column("ID",width=40)
tree.column("First Name", width=100)
tree.column("Last Name", width=100)
tree.column("DOB",width=90 )
tree.column("Client ID",width=70 )
tree.column("Email", width=200)
tree.column("Number", width=90)
tree.column("Street", width=80)
tree.column("City", width=80)
tree.column("State",width=70)
tree.column("Country", width=90)
tree.column("Category", width=70)
tree.column("Zip Code", width=70)


show_data()

tree.bind("<Double-1>", edit_record)
root.mainloop()