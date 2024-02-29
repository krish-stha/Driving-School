from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from datetime import datetime

####MAKE WINDOW## ######
root=Tk()
root.geometry("1920x1080")
root.title('Dashboard')
root.config(bg="white")

conn = sqlite3.connect("real.db")
db = conn.cursor()
db.execute("""CREATE TABLE IF NOT EXISTS usersTable(
                usersId INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName varchar(255),
                lastName varchar(255),
                dob varchar(255),
                clientId integer,
                email varchar(255),
                number integer,
                street varchar(255),
                city varchar(255),
                state varchar(255),
                country varchar(255),
                category varchar(255),
                zipCode integer,
                status varchar(255)
                )""")
conn.commit()
conn.close()
  
def std():
    """
    Closes the current root window and opens the student window.
    
    This function closes the current root window and imports the 'student' module
    to open the student window. It's typically used for navigation from one interface
    to another within the application.

    Returns:
        None
    """
    root.destroy()
    import student

def form():
    """
    Opens a new window for user details entry and database operations.

    This function creates a new window using Tkinter's Toplevel class
    to allow users to enter their details. It also includes functionality
    for adding these details to a SQLite database and retrieving records.

    Returns:
        None
    """

    window=Toplevel()
    window.config()
    window.title('Details')
    window.geometry(f'860x400+450+195')
    
    def add():

        """
    Adds user details to the database after validation.

    Retrieves user-entered data from the entry fields, validates the input,
    including ensuring all fields are filled, correct date format, age above 16,
    email ends with '@gmail.com', valid phone number, and then inserts the data
    into the SQLite database and  updated the numbers of inquiries,ongoing Students.
    Returns:
    
        None
    """
        first_name_value=first_name_box.get()
        last_name_value=last_name_box.get()
        date_value=date_box.get() 
        client_id_value=client_id_box.get()
        email_value=email_box.get()
        phone_value=phone_box.get()
        street_value=street_box.get()
        state_value=state_box.get()
        country_value=country_box.get()
        city_value=city_box.get()
        zip_value=zip_box.get()  
        category_value=category_box.get()
        user_status="active"

        # Check if any required  field is empty
        if (first_name_value == '' or last_name_value == '' or client_id_value =='' or date_value == '' or email_value == '' or phone_value == '' or street_value == '' or category_value=='' or city_value== '' or state_value == '' or zip_value == '' or country_value == ''):
            messagebox.showerror('Error', 'All Fields Are Required.', parent=window)
            return

        # Check if first name and last name contain only alphabets
        # if not first_name_value.isalpha() or not last_name_value.isalpha() or not state_value.isalpha() or not country_value.isalpha() or not city_value.isalpha() or not category_value.isalpha():
        #     messagebox.showerror('Error', 'Recheck the given information.', parent=window)
        #     return

         # Check if date is in the correct format and the person is above 16 years old
        
        try:
            birth_date = datetime.strptime(date_value, '%Y-%m-%d')

        except ValueError:
            messagebox.showerror('Error', 'Date must be in YYYY-MM-DD format.', parent=window)
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
            messagebox.showerror('Error', 'Age must be 16 years or older to be registered.', parent=window)
            return

       # Check if email ends with '@gmail.com'
        if not email_value.lower().endswith('@gmail.com'):
            messagebox.showerror('Error', 'Email must end with @gmail.com.', parent=window)
            return

        # Check if phone number is a digit and has 10 digits
        if not phone_value.isdigit() or len(phone_value) != 10:
            messagebox.showerror('Error', 'Phone number must be a 10-digit number.', parent=window)
            return
        
        else:
            try:
                conn = sqlite3.connect("real.db")
                db = conn.cursor()
                db.execute(
                """INSERT INTO usersTable(firstName,lastName,dob,clientId,email,number,street,city,state,country,category,zipCode,status) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (first_name_value, last_name_value, date_value, client_id_value,email_value,phone_value,street_value,city_value,state_value,country_value,category_value,zip_value,user_status),
                )
                conn.commit()
                messagebox.showinfo("Success","Added  Successfully")

            except sqlite3.Error as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

            finally:
                db.close()
                conn.close()
                retrieve()
                # get_record_count()

            totalRecords = get_record_count()
            no_of_ongoing_students = get_active_record_count()
            no_of_closed_students = get_closed_record_count()

            inquriy_number.config(text=f'00{totalRecords}')
            ongoing_number.config(text=f'00{no_of_ongoing_students}')
            closed_number.config(text=f'00{no_of_closed_students}')

    def retrieve():
        """
    Find user records from the database.

    This function queries the SQLite database to retrieve all user records
    and prints them to the console.

    Returns:
        None
    """
        try:
            conn = sqlite3.connect("real.db")
            db = conn.cursor()

            db.execute("SELECT * FROM usersTable")

            records = db.fetchall()
            

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        finally:
            db.close()
            conn.close()

    ##########Personal details UI ######

    personal = Label(window,text="PERSONAL DETAILS",border=5,font=("arial rounded MT Bold",10,"bold"),fg="#3985FF").place(x=10, y=10)

    first_name = Label(window,text="First Name",font=("arial rounded MT Bold",8)).place(x=10, y=50)
    first_name_box = Entry(window,width=40)
    first_name_box.place(x=10, y=70)

    last_name = Label(window,text="Last Name",font=("arial rounded MT Bold",8)).place(x=300, y=50)
    last_name_box = Entry(window,width=40)
    last_name_box.place(x=300, y=70)
    
    date = Label(window,text="D.O.B",font=("arial rounded MT Bold",8)).place(x=10, y=100)
    date_box = Entry(window, width=40)
    date_box.place(x=10, y=120)
    instruction = Label(window,text="Date must be in YYYY-MM-DD[2012-12-22]format",font=("arial rounded MT Bold",7)).place(x=10, y=140)

    Client_id = Label(window,text="Citizenship ID",font=("arial rounded MT Bold",8)).place(x=300, y=100)
    client_id_box = Entry(window,width=40)
    client_id_box.place(x=300, y=120)

    email = Label(window,text="Email",font=("arial rounded MT Bold",8)).place(x=600,y=50)
    email_box = Entry(window,width=40)
    email_box.place(x=600, y=70)
    
    phone = Label(window,text="Phone",font=("arial rounded MT Bold",8)).place(x=600,y=100)
    phone_box = Entry(window,width=40)
    phone_box.place(x=600, y=120)

    street = Label(window,text="Street",font=("arial rounded MT Bold",8)).place(x=10,y=180)
    street_box = Entry(window,width=40)
    street_box.place(x=10, y=200)

    city = Label(window,text="City",font=("arial rounded MT Bold",8)).place(x=300,y=180)
    city_box = Entry(window,width=40)
    city_box.place(x=300, y=200)

    state = Label(window,text="State",font=("arial rounded MT Bold",8)).place(x=600,y=180)
    state_box = Entry(window,width=40)
    state_box.place(x=600, y=200)

    zip = Label(window,text="Zip/Post Code",font=("arial rounded MT Bold",8)).place(x=10,y=250)
    zip_box = Entry(window,width=40)
    zip_box.place(x=10, y=270)

    country = Label(window,text="Country",font=("arial rounded MT Bold",8)).place(x=300,y=250)
    country_box = Entry(window,width=40)
    country_box.place(x=300, y=270)
    
    category=Label(window,text="Category",font=("arial rounded MT Bold",8)).place(x=600,y=250)
    category_box = Entry(window,width=40)
    category_box.place(x=600,y=270)

    add_button=Button(window,text="Add",cursor='hand2',font=("arial rounded MT Bold",12,"bold"),height=2,width=15,activebackground="#3985FF",bg="#3985FF",fg="white",command=add)
    add_button.place(x=350,y=320)

    root.mainloop()

def get_record_count():
        """
    Get the total count of records in the database.

    This function connects to the 'real.db' database and queries the 'usersTable'
    to count the total number of records. It then returns this count.

    Returns:
        int: The total count of records in the database.
    """
        global no_of_inquiry
        global no_of_ongoing_students
        no_of_inquiry=""
        conn = sqlite3.connect("real.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM usersTable")
        count = cursor.fetchone()[0]

        conn.close()
        return count
    
def get_active_record_count():
        """
    Bring the count of records in the database that are active.

    This function connects to the 'real.db' database and queries the 'usersTable'
    to count the number of records where the status is 'active'. It then returns
    this count.

    Returns:
        int: The count of active records in the database.
    """
        global no_of_inquiry
        global no_of_ongoing_students
        no_of_inquiry=""
        conn = sqlite3.connect("real.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM usersTable WHERE status = 'active'")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
def get_closed_record_count():
        """
    fetch the count of records in the database that are not active.

    This function connects to the 'real.db' database and queries the 'usersTable'
    to count the number of records where the status is not 'active'. It then returns
    this count.

    Returns:
        int: The count of closed records in the database.
    """
        global no_of_inquiry
        global no_of_ongoing_students
        no_of_inquiry=""
        conn = sqlite3.connect("real.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM usersTable WHERE status != 'active'")
        count = cursor.fetchone()[0]
        conn.close()

        return count

totalRecords=get_record_count()
no_of_ongoing_students=get_active_record_count()
no_of_closed_students=get_closed_record_count()

# # dashboard UI##

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
    """
    user_menu.post(event.x_root, event.y_root)

profile_image = PhotoImage(file="b.png")

# Create a profile icon button with the image
profile_icon_button = Button(root, cursor='hand2', image=profile_image, bd=0, bg="white", width=32, height=32)
profile_icon_button.place(x=1420, y=10)

# Create a menu for the user
user_menu = Menu(root, tearoff=0, bg="lightgray", fg="black", font=("Helvetica", 10, "bold"))

user_menu.add_command(label="Sign out", font=("Helvetica", 10, "bold"), command=signOut)

# Bind the menu to the profile icon button
profile_icon_button.bind("<Button-1>", show_user_menu)

add_student=Button(root,cursor='hand2',text="Add Student",bg="#3985FF",fg="white",height=2,width=15,activebackground="#3985FF",command=form)
add_student.place(x=370,y=15)

big_label=Label(root,height=55,width=50,bg="#152844")
big_label.place(x=0)

right_label=Label(root,height=50,width=170,bg="white")
right_label.place(x=356,y=70)

#LEFT LABEL

home_image = Image.open("home_icon.png")  
home_photo = ImageTk.PhotoImage(home_image)
home_image_label=Label(big_label,image=home_photo,bg="#152844")
home_image_label.place(x=17,y=495)

home=Button(big_label,cursor='hand2',text="Home",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844")
home.place(x=60,y=500)

student_image = Image.open("student_icon.png")  
student_photo = ImageTk.PhotoImage(student_image)
student_image_label=Label(big_label,image=student_photo,bg="#152844")
student_image_label.place(x=17,y=555)

student=Button(big_label,cursor='hand2',text="Student",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=std)
student.place(x=60,y=560)

def setting():
    
    """
    Function to handle payment process.

    This function destroys the Tkinter root window, typically used for the GUI,
    and then imports the 'invo' module .
    """
    root.destroy()
    import invo

setting_image = Image.open("setting_icon.png")  
setting_photo = ImageTk.PhotoImage(setting_image)
image_label=Label(big_label,image=setting_photo,bg="#152844")
image_label.place(x=17,y=615)

setting1=Button(big_label,cursor='hand2',text="Setting",font=("arial rounded MT Bold",15),bg="#152844",fg="white",bd=0,activebackground="#152844",command=setting)
setting1.place(x=60,y=620)

##### 3 box ####

inquiry=Label(right_label, height=20, width=45, relief="sunken",bg="white",bd=3)
inquiry.place(x=50, y=220)

inq_image = Image.open("people icon.png")  
inq_photo = ImageTk.PhotoImage(inq_image)
image_label=Label(right_label,image=inq_photo,bg="white")
image_label.place(x=100,y=360)

inquriy_number=Label(right_label,text=f'00{totalRecords}',font=("Arial", 40),bd=0,bg="white")
inquriy_number.place(x=180,y=350)

inquiry_text=Label(right_label, height=5, width=46,text="Number Of Inquiries",fg="white",font=("arial rounded MT Bold",8), relief="ridge",bg="#3985FF")
inquiry_text.place(x=50, y=520)


ongoing=Label(right_label, height=20, width=45, bg="white",relief="sunken", bd=3)
ongoing.place(x=430, y=220)

image_label=Label(right_label,image=inq_photo,bg="white")
image_label.place(x=480,y=360)

ongoing_number=Label(right_label,text=f'00{no_of_ongoing_students}',font=("Arial", 40),bd=0,bg="white")
ongoing_number.place(x=560,y=350)

ongoing_text=Label(right_label, height=5, text="Number Of Ongoing Students",fg="white",font=("arial rounded MT Bold",8),width=46, bg="#3985FF", bd=1, relief="ridge")
ongoing_text.place(x=430, y=520)


closed=Label(right_label, height=20, width=45,bg="white",relief="sunken", bd=3)
closed.place(x=800, y=220)

image_label=Label(right_label,image=inq_photo,bg="white")
image_label.place(x=850,y=360)

closed_number=Label(right_label,text=f'00{no_of_closed_students}',font=("Arial", 40),bd=0,bg="white")
closed_number.place(x=930,y=350)

closed_text=Label(right_label, height=5,text="Number Of Closed Students",fg="white",font=("arial rounded MT Bold",8), width=46, bg="#3985FF", bd=1, relief="ridge")
closed_text.place(x=800, y=520)


image = Image.open("drivelogo.png")  
photo = ImageTk.PhotoImage(image)
image_label=Label(big_label,image=photo,bg="#152844")
image_label.place(x=17,y=10)

pro=Label(big_label,text="Pro Driving Academy",font=("arial rounded MT bold",13,"bold"),fg="white",bg="#152844")
pro.place(x=78,y=100)

root.mainloop()


##########END########