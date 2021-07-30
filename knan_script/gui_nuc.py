
from tkinter import *
import tkinter as tk
from  change_ftdi_knan_name import *
from tkinter import filedialog
table_name ="main"
displayed_columns="id, device, pcb_main, c_sensor ,c_oled, note"
global cursor

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

    print("Record inserted successfully into Laptop table")

# https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# 43:57
def update_row():
     print("update row")



# https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# 43:57
def delete_row():
    print("delete_row")


def submitact():
    user = Username.get()
    passw = password.get()
    logintodb(user, passw)

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

root = Tk()

def brow_folder_cb():
    print("Refreshing table")
    #root.withdraw()
    file_path_variable = search_for_file_path()
    print ("\nfile_path_variable = ", file_path_variable)

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i )

def search():
    q2 = q.get()
    query = "SELECT "+displayed_columns+" FROM "+table_name+" WHERE device LIKE '%"+q2+"%' OR pcb_main LIKE '%"+q2+"%'"


def getrow(event):
    global selected_id


def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir



wrapper0 = LabelFrame(root, text="Login")
wrapper1 = LabelFrame(root, text=table_name)
wrapper2 = LabelFrame(root, text="User action")
wrapper3 = LabelFrame (root, text="Customer Data")

wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

query = "SELECT "+displayed_columns+" from "+table_name


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
btn_browse_dir = tk.Button(wrapper2, text ="BROWSE_DIR", 
                       bg ='blue', command = brow_folder_cb)
btn_browse_dir.place(x = 20, y = 20, width = 75)

#Search selection
q=StringVar()
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

addrecordButton = tk.Button(wrapper3, text ="CHECK_NUC_FOLDER", 
                       bg ='blue', command = main_check_complete_nuc_folder)

addrecordButton.grid(row = 2, column=0, pady = 20)

updateButton = tk.Button(wrapper3, text ="CHANGE_NAME", 
                       bg ='blue', command = main_check_and_change_nucfolder_name)

updateButton.grid(row = 3, column=0, pady = 20)

deleteButton = tk.Button(wrapper3, text ="DELETE", 
                       bg ='blue', command = delete_row)

deleteButton.grid(row = 4, column=0, pady = 20)

root.title("KNAN NUC check tool")
root.geometry("1200x800")
#root.resizable(False, False)
root.mainloop()