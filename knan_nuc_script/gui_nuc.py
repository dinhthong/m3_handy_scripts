
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
from configparser import ConfigParser
from change_ftdi_knan_name import *
from copy_nuc_data import *
from nuc_production import *
#full_app_data_path = os.getcwd()+"\\...\\..."
full_app_data_path = os.getcwd()
os.chdir('..')
os.chdir('..')
full_app_data_path = os.getcwd()
pg_textfile_name = os.path.join(full_app_data_path, "config.ini")
print(pg_textfile_name)
config = ConfigParser()
# check and write text file
if os.path.exists(pg_textfile_name):
    print("Config already exists")
else:
    f = open(pg_textfile_name,"w+")
    f.close()

config.read(pg_textfile_name)

if config.has_section('main') == False:
    print("config.has_section('main') == False")
    config.add_section('main')
    config.set('main', 'nuc_base_dir', "")
    config.set('main', 'software_folder', "")
def submitact():
    user = Username.get()
    passw = password.get()
    #logintodb(user, passw)

root = Tk()

# def btn_org_dir_cb():
#     #print("Refreshing table")
#     file_path_variable = search_for_file_path(dir_org_q.get())
#     print ("\nfile_path_variable = ", file_path_variable)
#     if file_path_variable != "":
#         dir_org_q.set(file_path_variable)
#         # write to config file
#         # config.add_section('main')
#         config.set('main', 'nuc_base_dir', file_path_variable)
#         status_q.set("Change folder contains NUC folders to: " + file_path_variable)

# def btn_soft_dir_cb():
#     #print("Refreshing table")
#     file_path_variable = search_for_file_path(dir_soft_q.get())
#     print ("\nfile_path_variable = ", file_path_variable)
#     if file_path_variable != "":
#         dir_soft_q.set(file_path_variable)
#         # write to config file
#         # config.add_section('main')
#         config.set('main', 'software_folder', file_path_variable)
#         status_q.set("Change folder contains KNAN_Software to: " + file_path_variable)

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

# working log on GUI
status_q = StringVar()
status_q.set("HELLO")
lbl = Label(wrapper1, width=50, textvariable = status_q)
lbl.pack(side=tk.LEFT, padx=15)

def search_btn_cb():
    print("Search button clicked")
class select_dir_button:
    button_text = 0
    config_file_key = ""
    dir_q = StringVar()
    btn_soft_object = tk.Button()
    ent_data = Entry()
    y_pos = 0
    x_pos = 0
    # parameterized constructor
    def __init__(self, _btn_text, _config_file_key):
        self.button_text = _btn_text
        self.config_file_key = _config_file_key
        self.btn_soft_object = tk.Button(wrapper2, text = self.button_text, 
                       bg ='blue', command = self.btn_select_dir_cb)
        self.dir_q.set(config.get('main', _config_file_key))
    # Button
    def place_button(self, _x, _y, _width):
        self.x_pos = _x
        self.y_pos = _y
        self.btn_soft_object.place(x = _x, y = _y, width = _width)

    ent_data = Entry(wrapper2, textvariable = dir_q)
    # Textbox
    def place_textbox(self, _x, _h, _w, _y = y_pos):
        self.ent_data.pack(side=tk.LEFT, padx=6)
        self.ent_data.place(x=_x, y=_y, height=_h, width=_w)
    
    def btn_select_dir_cb(self):
        #print("Refreshing table")
        file_path_variable = search_for_file_path(self.dir_q.get())
        print ("\nfile_path_variable = ", file_path_variable)
        if file_path_variable != "":
            self.dir_q.set(file_path_variable)
            # write to config file
            # config.add_section('main')
            config.set('main', self.config_file_key, file_path_variable)
            status_q.set("Change folder contains "+ self.button_text + " to: " + file_path_variable)

org_field = select_dir_button("ORG", 'nuc_base_dir')
org_field.place_button(10, 10, 75)
org_field.place_textbox(_x = 500, _h = 20, _w = 350)

soft_field = select_dir_button("SOFT_DIR", 'software_folder')
soft_field.place_button(400, 40, 75)
soft_field.place_textbox(_x = 200, _h = 40, _w = 350)

# create new record wrapper
# https://www.kite.com/python/answers/how-to-make-an-array-of-strings-in-python
ftdi_dev_pair_json_dir = "ftdi_dev_pair.json"

def btn_main_check_complete_nuc_folder():
    print(org_field.dir_q.get())
    main_check_complete_nuc_folder(org_field.dir_q.get())
    status_q.set("Done btn_main_check_complete_nuc_folder!")

def btn_extract_and_save_nuc_folder_info_to_json_file():
    print(org_field.dir_q.get())
    extract_and_save_nuc_folder_info_to_json_file(org_field.dir_q.get(), ftdi_dev_pair_json_dir)

def btn_main_check_and_change_nucfolder_name():
    print(org_field.dir_q.get())
    main_check_and_change_nucfolder_name(org_field.dir_q.get())

def btn_remove_status_msg_from_nuc_folder_name():
    #print(dir_org_q.get())
    remove_status_msg_from_nuc_folder_name(org_field.dir_q.get())
    status_q.set("Done btn_remove_status_msg_from_nuc_folder_name!")

def btn_arrange_nuc_files_to_folder():
    #print(dir_org_q.get())
    arrange_nuc_files_to_folder(soft_field.dir_q.get())
    status_q.set("Done btn_remove_status_msg_from_nuc_folder_name!")

def btn_arrange_nuc_files_firstlevel_subfolders():
    arrange_nuc_files_in_firstlevel_subfolder(soft_field.dir_q.get())
    status_q.set("Done btn_arrange_nuc_files_firstlevel_subfolders_to_folder!")

def btn_extract_nucfiles_in_soft():
    extract_files_in_childfolders(soft_field.dir_q.get())
    status_q.set("Done btn_extract_nucfiles_in_soft!")
# Define buttons
btn_CHANGE_FOLDER_NAME_IN_ORG = tk.Button(wrapper3, text ="1. CHANGE_FOLDER_NAME_IN_ORG", 
                       bg ='#ffb3fe', command = btn_main_check_and_change_nucfolder_name)

btn_CHANGE_FOLDER_NAME_IN_ORG.grid(row = 2, column=2, pady = 20)

btn_get_ftdi_and_dev_pair = tk.Button(wrapper3, text ="2.0. GET NUC FOLDER INFO TO JSON", 
                       bg ='#ffb3fe', command = btn_extract_and_save_nuc_folder_info_to_json_file)

btn_get_ftdi_and_dev_pair.grid(row = 3, column=2, pady = 20)

btn_checknuc = tk.Button(wrapper3, text ="2.1. CHECK_NUC_FOLDER_IN_ORG", 
                       bg ='#ffb3fe', command = btn_main_check_complete_nuc_folder)

btn_checknuc.grid(row = 4, column = 2, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="3. REMOVE_STATUS_MSG_IN_ORG", 
                       bg ='#ffb3fe', command = btn_remove_status_msg_from_nuc_folder_name)

btn_rm_status_msg.grid(row = 5, column=2, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="4. ARRANGE_NUC_FILES_TO_FOLDER_IN_SOFT", 
                       bg ='#ffb3fe', command = btn_arrange_nuc_files_to_folder)

btn_rm_status_msg.grid(row = 3, column= 3, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="5. ARRANGE_NUC_FILES_IN_FIRSTLEVEL_SOFT", 
                       bg ='#ffb3fe', command = btn_arrange_nuc_files_firstlevel_subfolders)

btn_rm_status_msg.grid(row = 4, column= 3, pady = 20)

btn_rm_status_msg = tk.Button(wrapper3, text ="6. EXTRACT_NUC_FILES_IN_SOFT", 
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