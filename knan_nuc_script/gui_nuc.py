
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
from configparser import ConfigParser
from change_ftdi_knan_name import *
from copy_nuc_data import *
from nuc_production import *
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
    print("config.has_section('main') == False")
    config.add_section('main')
    config.set('main', 'nuc_base_dir', "")
    config.set('main', 'software_folder', "")
    config.set('main', 'knandata_folder', "")
def submitact():
    user = Username.get()
    passw = password.get()
    #logintodb(user, passw)

root = Tk()

def btn_org_dir_cb():
    #print("Refreshing table")
    file_path_variable = search_for_file_path(dir_org_q.get())
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_org_q.set(file_path_variable)
        # write to config file
        # config.add_section('main')
        config.set('main', 'nuc_base_dir', file_path_variable)
        status_q.set("Change folder contains NUC folders to: " + file_path_variable)

def btn_soft_dir_cb():
    #print("Refreshing table")
    file_path_variable = search_for_file_path(dir_soft_q.get())
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_soft_q.set(file_path_variable)
        # write to config file
        # config.add_section('main')
        config.set('main', 'software_folder', file_path_variable)
        status_q.set("Change folder contains KNAN_Software to: " + file_path_variable)

def btn_des_dir_cb():
        #print("Refreshing table")
    file_path_variable = search_for_file_path(dir_des_q.get())
    print ("\nfile_path_variable = ", file_path_variable)
    if file_path_variable != "":
        dir_des_q.set(file_path_variable)
        # write to config file
        # config.add_section('main')
        config.set('main', 'knandata_folder', file_path_variable)
        status_q.set("Change folder contains KNAN_Software to: "+file_path_variable)

def search_for_file_path(current_dir):
    #currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=current_dir, title='Please select a directory')
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
btn_org_dir_object = tk.Button(wrapper2, text ="ORG_DIR", 
                       bg ='blue', command = btn_org_dir_cb)
btn_org_dir_object.place(x = 10, y = 10, width = 75)
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
dir_org_q = StringVar()
# lbl = Label(wrapper2, width=10, text="Selected dir")
# lbl.pack(side=tk.LEFT, padx=15)
ent2 = Entry(wrapper2, textvariable=dir_org_q)
ent2.pack(side=tk.LEFT, padx=6)
ent2.place(x=100, y=15, height=20, width=350)
dir_org_q.set(config.get('main', 'nuc_base_dir'))

# data_folder selection
btn_soft_dir_object = tk.Button(wrapper2, text ="SOFT_DIR", 
                       bg ='blue', command = btn_soft_dir_cb)
btn_soft_dir_object.place(x = 500, y = 40, width = 75)

dir_soft_q = StringVar()
ent_data = Entry(wrapper2, textvariable=dir_soft_q)
ent_data.pack(side=tk.LEFT, padx=6)
ent_data.place(x=600, y=40, height=20, width=350)
dir_soft_q.set(config.get('main', 'software_folder'))

# KNAN_software/data folder
btn_des_dir_object = tk.Button(wrapper2, text ="DES_DIR", 
                       bg ='blue', command = btn_des_dir_cb)
btn_des_dir_object.place(x = 500, y = 65, width = 75)

dir_des_q = StringVar()
ent3 = Entry(wrapper2, textvariable=dir_des_q)
ent3.pack(side=tk.LEFT, padx=6)
ent3.place(x=600, y=65, height=20, width=350)
dir_des_q.set(config.get('main', 'knandata_folder'))

# working log on GUI
status_q = StringVar()
status_q.set("HELLO")
lbl = Label(wrapper1, width=50, textvariable = status_q)
lbl.pack(side=tk.LEFT, padx=15)

# create new record wrapper
# https://www.kite.com/python/answers/how-to-make-an-array-of-strings-in-python

def btn_main_check_complete_nuc_folder():
    print(dir_org_q.get())
    main_check_complete_nuc_folder(dir_org_q.get())
    status_q.set("Done btn_main_check_complete_nuc_folder!")

def btn_main_check_and_change_nucfolder_name():
    print(dir_org_q.get())
    main_check_and_change_nucfolder_name(dir_org_q.get())

def btn_remove_status_msg_from_nuc_folder_name():
    #print(dir_org_q.get())
    remove_status_msg_from_nuc_folder_name(dir_org_q.get())
    status_q.set("Done btn_remove_status_msg_from_nuc_folder_name!")

def btn_arrange_nuc_files_to_folder():
    #print(dir_org_q.get())
    arrange_nuc_files_to_folder(dir_soft_q.get())
    status_q.set("Done btn_remove_status_msg_from_nuc_folder_name!")

def btn_arrange_nuc_files_firstlevel_subfolders():
    arrange_nuc_files_in_firstlevel_subfolder(dir_soft_q.get())
    status_q.set("Done btn_arrange_nuc_files_firstlevel_subfolders_to_folder!")
def btn_extract_nucfiles_in_soft():
    extract_files_in_childfolders(dir_soft_q.get())
    status_q.set("Done btn_extract_nucfiles_in_soft!")
# Define buttons
btn_CHANGE_FOLDER_NAME_IN_ORG = tk.Button(wrapper3, text ="CHANGE_FOLDER_NAME_IN_ORG", 
                       bg ='#ffb3fe', command = btn_main_check_and_change_nucfolder_name)

btn_CHANGE_FOLDER_NAME_IN_ORG.grid(row = 2, column=2, pady = 20)

btn_checknuc = tk.Button(wrapper3, text ="CHECK_NUC_FOLDER_IN_ORG", 
                       bg ='#ffb3fe', command = btn_main_check_complete_nuc_folder)

btn_checknuc.grid(row = 3, column=2, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="REMOVE_STATUS_MSG_IN_ORG", 
                       bg ='#ffb3fe', command = btn_remove_status_msg_from_nuc_folder_name)

btn_rm_status_msg.grid(row = 4, column=2, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="ARRANGE_NUC_FILES_TO_FOLDER_IN_SOFT", 
                       bg ='#ffb3fe', command = btn_arrange_nuc_files_to_folder)

btn_rm_status_msg.grid(row = 3, column= 3, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="ARRANGE_NUC_FILES_IN_FIRSTLEVEL_SOFT", 
                       bg ='#ffb3fe', command = btn_arrange_nuc_files_firstlevel_subfolders)

btn_rm_status_msg.grid(row = 4, column= 3, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="EXTRACT_NUC_FILES_IN_SOFT", 
                       bg ='#ffb3fe', command = btn_extract_nucfiles_in_soft)

btn_rm_status_msg.grid(row = 6, column= 3, pady = 20)

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