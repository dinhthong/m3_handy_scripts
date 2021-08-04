# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json
import shutil

# define constant
c_ftdi_length = 8
# global vars
extracted_ftdi = ""
item_fullpath = ""
underscore_index_list = []
allow_print_debug_info = 0
g_allow_rename = 1

def print_debug(s):
	if allow_print_debug_info==1:
		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)

# -20, -10, 0,...
temp_file_check = array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])


ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0

check_folder_content_ok_flag = 0


each_item_folder_ls_list = []
# Create if not exist
def create_data_FTDI_folder(base, ftdi):
	#get_datetime_string()
	ftdi_folder_path = base + "/data_" + ftdi
	try:
		os.mkdir(ftdi_folder_path) 
	except OSError as error: 
		print(error)
	

def check_file_count(file_count):
	print("File count: " + str(file_count))
	if file_count == 0:
		print_fail("Folder empty!")
	else:
		if file_count == 15:
			print_ok("File count ok")
		else:
			print_fail("File count error")

json_file_name = ""

def create_ftdi_folders_and_move_ftdi_files(base_dir, folder_ls_list):
	count = 1
	for each_item_folder_name in folder_ls_list:
		print_header("***STT: " + str(count))
		count = count + 1
		item_fullpath = base_dir + '/' + each_item_folder_name
		print(item_fullpath)
		if os.path.isfile(item_fullpath) == True:
			status, extracted_ftdi = get_full_ftdi_from_file_name(each_item_folder_name)
			if status == 1:
				print("Extracted ftdi: " + extracted_ftdi)
				create_data_FTDI_folder(base_dir, extracted_ftdi)
				file_type = check_file_name_and_size(each_item_folder_name, get_file_size(item_fullpath))
				new_file_path = base_dir + '/' + "data_" + extracted_ftdi + '/' + each_item_folder_name
				os.rename(item_fullpath, new_file_path)
		print_header("--------------------------------------------------------------------------------------------")

def copy_from_nuc_data_folder_to_des(knan_software_dir, _des_folder):
	global item_fullpath
	global each_item_folder_ls_list
	root_folder_ls_list = os.listdir(knan_software_dir)
	create_ftdi_folders_and_move_ftdi_files(knan_software_dir, root_folder_ls_list)
	# check files in each folder
	
def main():
	copy_from_nuc_data_folder_to_des("D:\py_test_KNAN_software", "D:\py_test_des_folder")
if __name__ == "__main__":
    main()