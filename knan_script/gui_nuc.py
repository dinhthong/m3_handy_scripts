
from tkinter import *
import tkinter as tk
from  change_ftdi_knan_name import *
from tkinter import filedialog
import os
c_machine_type = 1 # 0 for ubuntu (windows subsystem for windows), 1 for windows

if c_machine_type == 0:
	#_filename = '/mnt/e/du lieu nuc knan '
	_filename = '/mnt/d/Dulieu_NUC_KNAN/HDD_1TB_29July21'
else:
	_filename = "D:\Dulieu_NUC_KNAN\HDD_1TB_29July21"

pg_textfile_name = "config.txt"
# check and write text file
if os.path.exists(pg_textfile_name):
    print("adding new record")

# This function should be improved later:
# main -> table variable
# number of input vars is automatically read from table 
def add_new_record():
    print("adding new record")
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
    #logintodb(user, passw)

root = Tk()

def brow_folder_cb():
    print("Refreshing table")
    file_path_variable = search_for_file_path()
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_q.set(file_path_variable)
        # write to config file

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

wrapper0 = LabelFrame(root, text="Login")
wrapper1 = LabelFrame(root, text="main")
wrapper2 = LabelFrame(root, text="User action")
wrapper3 = LabelFrame (root, text="Customer Data")

wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

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
 
# User action wrapper
btn_browse_dir = tk.Button(wrapper2, text ="BROWSE_DIR", 
                       bg ='blue', command = brow_folder_cb)
btn_browse_dir.place(x = 20, y = 20, width = 75)

def search_btn_cb():
    print("Search button clicked")
#Search selection
# Search box
q=StringVar()
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
# Search button
btn = Button(wrapper2, text="Search", command=search_btn_cb)
btn.pack(side=tk.LEFT, padx=6) 

# Search box
dir_q = StringVar()
lbl = Label(wrapper2, width=10, text="Selected dir")
lbl.pack(side=tk.LEFT, padx=15)
ent2 = Entry(wrapper2, textvariable=dir_q)
ent2.pack(side=tk.LEFT, padx=6)
ent2.place(x=100, y=15, height=20, width=350)
# Search button
#btn = Button(wrapper2, text="Search", command=search)
#btn.pack(side=tk.LEFT, padx=6) 

# create new record wrapper
# https://www.kite.com/python/answers/how-to-make-an-array-of-strings-in-python

def btn_main_check_complete_nuc_folder():
    print(dir_q.get())
    main_check_complete_nuc_folder(dir_q.get())

def btn_main_check_and_change_nucfolder_name():
    print(dir_q.get())
    main_check_and_change_nucfolder_name(dir_q.get())

def btn_remove_status_msg_from_nuc_folder_name():
    #print(dir_q.get())
    remove_status_msg_from_nuc_folder_name(dir_q.get())

btn_change_name = tk.Button(wrapper3, text ="CHANGE_NAME", 
                       bg ='blue', command = btn_main_check_and_change_nucfolder_name)

btn_change_name.grid(row = 2, column=0, pady = 20)

btn_checknuc = tk.Button(wrapper3, text ="CHECK_NUC_FOLDER", 
                       bg ='blue', command = btn_main_check_complete_nuc_folder)

btn_checknuc.grid(row = 3, column=0, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="REMOVE_STATUS_MSG", 
                       bg ='blue', command = btn_remove_status_msg_from_nuc_folder_name)

btn_rm_status_msg.grid(row = 4, column=0, pady = 20)

root.title("KNAN NUC check tool")
root.geometry("1200x800")
#root.resizable(False, False)
root.mainloop()