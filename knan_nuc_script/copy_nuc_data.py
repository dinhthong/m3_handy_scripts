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
underscore_index_list = []
allow_print_debug_info = 0

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
# Description: check file name and file size 
def check_temperature_file(_nuc_file_fullpath):
	if os.path.isfile(_nuc_file_fullpath):
		return True
	else: 
		print("Not file")
# _paren_folder: D:\py_test_KNAN_software
def extract_files_in_childfolders_to_des(_paren_folder, _des_folder):
	count = 1
	root_folder_ls_list = os.listdir(_paren_folder)
	# each_item_folder_name: 056_FT5OV9NG_ok
	for each_item_folder_name in root_folder_ls_list:
		print_header("***STT: " + str(count))
		count = count + 1
		nuc_folder_fullpath = _paren_folder + '/'+  each_item_folder_name
		if os.path.isdir(nuc_folder_fullpath) == True:
			nuc_folder_fullpath_ls = os.listdir(nuc_folder_fullpath)
			for each_nuc_file in nuc_folder_fullpath_ls:
				nuc_file_fullpath = nuc_folder_fullpath +'/' + each_nuc_file
				if check_temperature_file(nuc_file_fullpath) == True:
					new_file_path = _des_folder+'/'+each_nuc_file
					print("nuc_file_fullpath: " + nuc_file_fullpath)
					print("new_file_path: " + new_file_path)
					os.rename(nuc_file_fullpath, new_file_path)
		else:
			print_header("Not folder")
		#check_individual_nuc_folder_files(_base_dir_name, each_item_folder_name)
def arrange_nuc_files_to_folder(knan_software_dir):
	global each_item_folder_ls_list
	root_folder_ls_list = os.listdir(knan_software_dir)
	create_ftdi_folders_and_move_ftdi_files(knan_software_dir, root_folder_ls_list)
	# check files in each folder
	
def main():
	#arrange_nuc_files_to_folder("D:\py_test_KNAN_software", "D:\py_test_des_folder")
	extract_files_in_childfolders_to_des("D:\py_test_KNAN_software", "D:\py_test_des_folder")
if __name__ == "__main__":
    main()