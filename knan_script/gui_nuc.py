#youtube link: https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# Work with Tkinter Treeview Table with Search Feature | All Together in 1 Video | Worth Watching
from tkinter import *
import tkinter as tk
#import Tkinter
#import tkMessageBox
#import ttk
#import mysql.connector
#import PIL
table_name ="main"
displayed_columns="id, device, pcb_main, c_sensor ,c_oled, note"
global cursor

# def insertVariblesIntoTable(id, name, price, purchase_date):
#     try:
#         # connection = mysql.connector.connect(host='localhost',
#         #                                      database='Electronics',
#         #                                      user='pynative',
#         #                                      password='pynative@#29')
#         cursor = connection.cursor()
#         mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
#                                 VALUES (%s, %s, %s, %s) """

#         recordTuple = (id, name, price, purchase_date)
#         cursor.execute(mySql_insert_query, recordTuple)
#         connection.commit()
#         print("Record inserted successfully into Laptop table")

selected_id=""
# This function should be improved later:
# main -> table variable
# number of input vars is automatically read from table 
def add_new_record():
    print("adding new record")

    record_entry=[]
    for entries in my_entries:
        entry_list=record_entry.append(entries.get())
    print(record_entry)
    #Insert new records to table
    # for entries in my_entries:
    #     add_string=add_string+str(entries)+","
    mySql_insert_query = """INSERT INTO main (device, pcb_main, c_sensor, c_oled, note) 
                                VALUES (%s, %s, %s, %s, %s) """
    #recordTuple = (id, name, price, purchase_date)
    #insert_movies_query = """
    # INSERT INTO main (device, pcb_main, c_sensor, c_oled, note)
    # VALUES
    # ("++")
    # """
    #cursor.execute(mySql_insert_query, tuple(record_entry))

    #mydb.commit()
    #refresh_table()
    print("Record inserted successfully into Laptop table")

# https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# 43:57
def update_row():
     print("update row")
#     record_entry=[]
#     for entries in my_entries:
#         entry_list=record_entry.append(entries.get())
#     record_entry.append(selected_id)
#     print(record_entry)
#     if tkMessageBox.askyesno("Confirm", "Are You Sure Update?"):
#         update_query = """UPDATE main SET device=%s, pcb_main=%s, c_sensor=%s, c_oled=%s, note=%s WHERE id=%s
#                             """
#         cursor.execute(update_query, tuple(record_entry))
#         #clear()
#         refresh_table()
#     else:
#         return True
    #mydb.commit()

# https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# 43:57
def delete_row():
    print("delete_row")
#     if tkMessageBox.askyesno("Confirm", "Are You Sure Delete?"):
#         query = "DELETE FROM main WHERE id = "+str(selected_id)
#         #cursor.execute(query)
#         #clear()
#         refresh_table()
#     else:
#         return True
#     mydb.commit()

def submitact():
    user = Username.get()
    passw = password.get()
    logintodb(user, passw)

# def logintodb(user, passw):
#     global db
    
#     # If paswword is enetered by the 
#     # user
#     if passw:
#         db = mysql.connector.connect(host='127.0.0.1', #host ="localhost",
#                                      user = user,
#                                      password = passw,
#                                      db ="m3_knan")
#     cursor = db.cursor()

# def descb_table():
#     # A Table in the database
#     show_table_query = "DESCRIBE " +table_name

#     try:
#         cursor.execute(show_table_query)
#         myresult = cursor.fetchall()
         
#         # Printing the result of the
#         # query
#         #get table's number of columns
#         table_col_size = len(myresult)
 
#         for x in myresult:
#             print(x)
#         print("Query Excecuted successfully")
         
#     except:
#         #db.rollback()
#         print("Error occured")

def show_table():

    print("*Show table's content:")
    select_movies_query = "SELECT * FROM "+table_name

    try:
        # cursor.execute(select_movies_query)
        # myresult = cursor.fetchall()
        # row_size = cursor.rowcount
        print("There's "+str(row_size)+" rows in this table")
        #col_size = cursor.colcount
        #print("There's "+str(col_size)+" rows in this table")
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")

def refresh_table():

    print("Refreshing table")
    # select_movies_query = "SELECT * FROM "+table_name+" LIMIT 10"
    # query = "SELECT "+displayed_columns+" from "+table_name
    # cursor.execute(query)
    # rows = cursor.fetchall()
    # update(rows)


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i )

def search():
    q2 = q.get()
    query = "SELECT "+displayed_columns+" FROM "+table_name+" WHERE device LIKE '%"+q2+"%' OR pcb_main LIKE '%"+q2+"%'"
    # cursor.execute(query)
    # rows = cursor.fetchall()
    # update(rows)
# event handler for treeview table

def getrow(event):
    global selected_id
    #rowid=trv.indentify_row(event.y)
    # item = trv.item(trv.focus())
    # selected_id=item['values'][0]
    # #print(selected_id)
    # for i in range(table_col_size-1):
    #     entry_text[i].set(item['values'][i+1])

#mydb = mysql.connector.connect(host="localhost", user="root", passwd="cxzzxcCC", database="m3_knan", auth_plugin="mysql_native_password")
#cursor = mydb.cursor() 

# Get table's information at startup
table_query = "DESCRIBE " +table_name

# cursor.execute(table_query)
# myresult = cursor.fetchall()
         
# Printing the result of the query
# get table's number of columns
#table_col_size = len(myresult)
#print("There's "+str(table_col_size)+" cols in this table")
table_query = "SELECT * FROM "+table_name

#cursor.execute(table_query)
#myresult = cursor.fetchall()

#table_row_size = cursor.rowcount
#print("There's "+str(table_row_size)+" rows in this table")
#column_titles = [i[0] for i in cursor.description]
#print(column_titles)

root = Tk()

wrapper0 = LabelFrame(root, text="Login")
wrapper1 = LabelFrame(root, text=table_name)
wrapper2 = LabelFrame(root, text="User action")
wrapper3 = LabelFrame (root, text="Customer Data")

wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
# height = number of rows to show in one view
#trv=ttk.Treeview(wrapper1, show="headings", height="5")
#print(list(range(1,table_col_size)))
# specify column size based on actual table's column size
# trv["column"] = list(range(1,table_col_size+1))
# trv.pack(side=LEFT) 
# trv.place(x=0, y=0)

#
# trv.heading(1, text="Customer ID")
# trv.heading(2, text="First Name")
# trv.heading(3, text="Last Name")
# trv.heading(4, text="Age")
# trv.heading('#0', width=50, minwidth=100)
# trv.heading('#1', width=150, minwidth=200)
# trv.heading('#2', width=150, minwidth=100)
# trv.heading('#3', width=150, minwidth=200)
# trv.heading('#4', width=150, minwidth=200)

# trv.bind('<Double 1>', getrow)

# yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
# yscrollbar.pack(side=RIGHT, fill="y")

# xscrollbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
# xscrollbar.pack(side=BOTTOM, fill="x")

#trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
#query = "SELECT id, first_name, last_name, age from "+table_name\
query = "SELECT "+displayed_columns+" from "+table_name
# cursor.execute(query)
# rows = cursor.fetchall()
# update(rows)

# Login form wrapper

lblfrstrow = tk.Label(wrapper0, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(wrapper0, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(wrapper0, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(wrapper0, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(wrapper0, text ="Login", 
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 70, width = 55)
 
# descbButton = tk.Button(wrapper0, text ="descb", 
#       bg ='blue', command = descb_table)
# descbButton.place(x = 300, y = 20, width = 55)

showButton = tk.Button(wrapper0, text ="SHOW", 
                       bg ='blue', command = show_table)
showButton.place(x = 300, y = 50, width = 55)

# User action wrapper
#Search selection
q=StringVar()

reFreshButton = tk.Button(wrapper2, text ="REFRESH", 
                       bg ='blue', command = refresh_table)
reFreshButton.place(x = 20, y = 50, width = 75)

lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6) 

# create new record wrapper
# multiple entry boxes
my_entries = []

# strings = []

# for i in range(3):
# Create a list of 3 empty strings

#     strings.append("")

# print(strings)
# https://www.kite.com/python/answers/how-to-make-an-array-of-strings-in-python
entry_text = []
# for cnt in range(table_col_size-1):
#     # Label each entry box
#     var = StringVar()
#     entry_text.append(var)
#     label_entry = tk.Label(wrapper3, text =str(column_titles[cnt+1]))
#     label_entry.grid(row = 0, column = cnt, pady=20, padx=5)
#     #lbl.pack(side=tk.LEFT, padx=10)
#     my_entry=Entry(wrapper3, textvariable=var)
#     my_entry.grid(row=1, column=cnt, pady=20, padx=5)
#     my_entries.append(my_entry)

addrecordButton = tk.Button(wrapper3, text ="ADD", 
                       bg ='blue', command = add_new_record)

addrecordButton.grid(row = 2, column=0, pady = 20)

updateButton = tk.Button(wrapper3, text ="UPDATE", 
                       bg ='blue', command = update_row)

updateButton.grid(row = 2, column=1, pady = 20)

deleteButton = tk.Button(wrapper3, text ="DELETE", 
                       bg ='blue', command = delete_row)

deleteButton.grid(row = 2, column=2, pady = 20)

root.title("My Application")
root.geometry("1200x800")
#root.resizable(False, False)
root.mainloop()

