
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from  change_ftdi_knan_name import *
from tkinter import filedialog
import os
from configparser import ConfigParser

pg_textfile_name = "config.ini"
config = ConfigParser()
# check and write text file
if os.path.exists(pg_textfile_name):
    print("Config already exists")
    # config.add_section('main')
    # config.set('main', 'key1', 'value1')
else:
    f = open(pg_textfile_name,"w+")
    f.close()
config.read(pg_textfile_name)
if config.has_section('main') == False:
    config.add_section('main')
    config.set('main', 'complete_nuc_parentfolder', "")
    config.set('main', 'software_folder', "")
def submitact():
    user = Username.get()
    passw = password.get()
    #logintodb(user, passw)

root = Tk()

def browse_folder_cb():
    #print("Refreshing table")
    file_path_variable = search_for_file_path()
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_q.set(file_path_variable)
        # write to config file
        # config.add_section('main')
        config.set('main', 'complete_nuc_parentfolder', file_path_variable)
        status_q.set("Change folder contains NUC folders to: "+file_path_variable)
def br_software_folder_cb():
    #print("Refreshing table")
    file_path_variable = search_for_file_path()
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_data_q.set(file_path_variable)
        # write to config file
        # config.add_section('main')
        config.set('main', 'software_folder', file_path_variable)
        status_q.set("Change folder contains KNAN_Software to: "+file_path_variable)
def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

wrapper0 = LabelFrame(root, text="Login")
wrapper1 = LabelFrame(root, text="main")
wrapper2 = LabelFrame(root, text="User action")
wrapper3 = LabelFrame (root, text="KNAN NUC TOOL")

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

def search_btn_cb():
    print("Search button clicked")

# User action wrapper
btn_browse_dir = tk.Button(wrapper2, text ="BROWSE_DIR", 
                       bg ='blue', command = browse_folder_cb)
btn_browse_dir.place(x = 20, y = 20, width = 75)
# Search selection
# Search box
q = StringVar()
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
dir_q.set(config.get('main', 'complete_nuc_parentfolder'))

# data_folder selection
btn_browse_softwarefolder_dir = tk.Button(wrapper2, text ="SOFT_DIR", 
                       bg ='blue', command = br_software_folder_cb)
btn_browse_softwarefolder_dir.place(x = 400, y = 50, width = 75)

dir_data_q = StringVar()
ent_data = Entry(wrapper2, textvariable=dir_data_q)
ent_data.pack(side=tk.LEFT, padx=6)
ent_data.place(x=500, y=55, height=20, width=350)
dir_data_q.set(config.get('main', 'software_folder'))

# working log on GUI
status_q = StringVar()
status_q.set("HELLO")
lbl = Label(wrapper1, width=50, textvariable = status_q)
lbl.pack(side=tk.LEFT, padx=15)

# create new record wrapper
# https://www.kite.com/python/answers/how-to-make-an-array-of-strings-in-python

def btn_main_check_complete_nuc_folder():
    print(dir_q.get())
    main_check_complete_nuc_folder(dir_q.get())
    status_q.set("Done btn_main_check_complete_nuc_folder!")

def btn_main_check_and_change_nucfolder_name():
    print(dir_q.get())
    main_check_and_change_nucfolder_name(dir_q.get())

def btn_remove_status_msg_from_nuc_folder_name():
    #print(dir_q.get())
    remove_status_msg_from_nuc_folder_name(dir_q.get())
    status_q.set("Done btn_remove_status_msg_from_nuc_folder_name!")

btn_change_name = tk.Button(wrapper3, text ="CHANGE_NAME", 
                       bg ='#ffb3fe', command = btn_main_check_and_change_nucfolder_name)

btn_change_name.grid(row = 2, column=1, pady = 20)

btn_checknuc = tk.Button(wrapper3, text ="CHECK_NUC_FOLDER", 
                       bg ='#ffb3fe', command = btn_main_check_complete_nuc_folder)

btn_checknuc.grid(row = 3, column=2, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="REMOVE_STATUS_MSG", 
                       bg ='#ffb3fe', command = btn_remove_status_msg_from_nuc_folder_name)

btn_rm_status_msg.grid(row = 4, column=3, pady = 20)

root.title("KNAN NUC check tool")
root.geometry("1200x800")
#root.resizable(False, False)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open('config.ini', 'w') as f:
            config.write(f)
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()