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

image_label=Button(root,image=photo1,cursor='hand2',bd=0,bg="white")
image_label.place(x=1420,y=10)


def search_students():
    # Get the search query from the entry widget
    search_query = entry.get()

    # Clear existing data in the Treeview
    for record in tree.get_children():
        tree.delete(record)

    # Perform the search operation in your database
    try:
        conn = sqlite3.connect("dri.db")
        db = conn.cursor()

        # Perform the search query in the database
        db.execute("SELECT * FROM usersData WHERE firstName LIKE ? OR lastName LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))
        searched_records = db.fetchall()

        # Insert the search results into the Treeview
        for record in searched_records:
            tree.insert('', 'end', values=record)

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred while searching: {e}")

    finally:
        db.close()
        conn.close()
        entry.delete(0, 'end')

def show_all_data():
    for record in tree.get_children():
        tree.delete(record)
    show_data()



big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)


show_all_button = Button(right_label, text="Show All Data", bg="#3985FF",cursor='hand2', fg="white",height=2,width=15,activebackground="#3985FF", bd=0, font=("arial rounded MT Bold",12,"bold"), command=show_all_data)
show_all_button.place(x=460, y=590)



image2 = Image.open("real.png") 
photo2 = ImageTk.PhotoImage(image2)

search_button = Button(root, image=photo2,bg="white",cursor='hand2',bd=0,height=35,activebackground="white",command=search_students)
search_button.place(x=525, y=15)

placeholder = "Search Contacts"


entry =Entry( root,width=15, font=("cabiler", 14,"bold"),fg="black",bd=0)  

entry.insert(0, placeholder)
entry.bind("<FocusIn>", lambda event: entry.delete(0, END) if entry.get() == placeholder else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if entry.get() == "" else None)
entry.config(fg='grey')  
entry.place(x=370,y=22)



#LEFT LABEL

def payment():
    root.destroy()
    import invo

home=Button(big_label,text="Home",cursor='hand2',font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=home)
home.place(x=40,y=500)

student=Button(big_label,text="Student",cursor='hand2',font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
student.place(x=40,y=560)



invoice=Button(big_label,text="Invoice",cursor='hand2',font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=payment)
invoice.place(x=40,y=620)


# stering image
image = Image.open("drivelogo.png")  
photo = ImageTk.PhotoImage(image)

image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=17,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",13,"bold"),fg="white",bg="#152844")
pro.place(x=78,y=100)




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
    editor.geometry(f'860x400+450+195')
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
    category=Label(editor,text="Category",font=("arial rounded MT Bold",8)).place(x=600,y=250)
    category_editor = Entry(editor,width=40)
    category_editor.place(x=600,y=270)

    


    
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
    category_editor.insert(0, values[11])
    zip_editor.insert(0, values[12])
    
    
      
    
    
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
                    category_editor.get(),
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



    def delete_record():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete.")
            return

        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected record?",parent=editor)
        if not confirm:
            return

        for item in selected_item:
            item_id = tree.item(item, "values")[0]
            conn = sqlite3.connect("dri.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usersData WHERE usersId=?", (item_id,))
            conn.commit()
            conn.close()
            tree.delete(item)

    
    def closed_record():
        editor.destroy()
            

   
    edit_button=Button(editor,text="Save",cursor='hand2',font=("arial rounded MT Bold",9,"bold"),height=2,width=15,activebackground="#3985FF",bg="#3985FF",fg="white",command=update_data)
    edit_button.place(x=340,y=310)

    delete_button=Button(editor,text="Delete",cursor='hand2',font=("arial rounded MT Bold",9,"bold"),height=2,width=15,activebackground="#3985FF",bg="#3985FF",fg="white",command=delete_record)
    delete_button.place(x=50,y=320)

    closed_button=Button(editor,text="Close",cursor='hand2',font=("arial rounded MT Bold",9,"bold"),height=2,width=15,activebackground="#3985FF",bg="#3985FF",fg="white",command=closed_record)
    closed_button.place(x=660,y=320)


#show data
def show_data():
    conn = sqlite3.connect("dri.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usersData")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()


tree = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "DOB", "Client ID", "Email", "Number", "Street", "City", "State", "Country", "Category", "Zip Code"), show="headings",height=25)
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







# ###################above orginal
