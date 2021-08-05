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

# -20, -10, 0,...
temp_file_check = array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])


ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0

check_folder_content_ok_flag = 0
each_item_folder_ls_list = []

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

# item_fullpath_list: [D:/py_test_KNAN_software\\data_FT5P145V', 'D:/py_test_KNAN_software\\data_FT5P31ZZ', 'D:/py_test_KNAN_software\\FT5P145V1.bin']
# full_des_dir: full destination folder
def create_ftdi_folders_and_move_ftdi_files(item_fullpath_list, full_des_dir):
	count = 1
	for full_item_dir in item_fullpath_list:
		print_header("***STT: " + str(count))
		count = count + 1
		#item_fullpath = base_dir + '/' + each_item_folder_name
		print(full_item_dir)
		last_part_of_dir = os.path.basename(os.path.normpath(full_item_dir))
		if os.path.isfile(full_item_dir) == True:
			get_ftdi_ok, extracted_ftdi = get_full_ftdi_from_file_name(full_item_dir)
			if get_ftdi_ok == 1:
				print("Extracted ftdi: " + extracted_ftdi)
				new_ftdi_folder = create_data_FTDI_folder(full_des_dir, extracted_ftdi)
				file_type = check_nuc_file_name_and_size(full_item_dir, get_file_size(full_item_dir))
				new_file_path = os.path.join(new_ftdi_folder, last_part_of_dir)
				rename_dir(full_item_dir, new_file_path)
		print_header("--------------------------------------------------------------------------------------------")
# Description: check file name and file size 
def check_temperature_file(_nuc_file_fullpath):
	if os.path.isfile(_nuc_file_fullpath):
		return True
	else: 
		print("Not file")

# _paren_folder: D:\py_test_KNAN_software
def extract_files_in_childfolders_to_des(_paren_folder, _des_folder):
	root_folder_ls_list = os.listdir(_paren_folder)
	# each_item_folder_name: 056_FT5OV9NG_ok
	jfilename= get_json_file_name()
	jsonFile = open(jfilename, "w")
	for each_item_folder_name in root_folder_ls_list:
		nuc_folder_fullpath = _paren_folder + '/'+  each_item_folder_name
		if os.path.isdir(nuc_folder_fullpath) == True:
			nuc_folder_fullpath_ls = os.listdir(nuc_folder_fullpath)
			count = 0
			for each_nuc_file in nuc_folder_fullpath_ls:
				json_info_dict = {}
				count = count + 1
				print_header("***STT: " + str(count))
				json_info_dict['STT'] = count
				nuc_file_fullpath = nuc_folder_fullpath +'/' + each_nuc_file
				print(nuc_file_fullpath)
				if check_temperature_file(nuc_file_fullpath) == True:
					#json_info_dict['md5'] = get_md5_hash(nuc_file_fullpath)
					print("nuc_file_fullpath: " + nuc_file_fullpath)
					json_info_dict['original_path'] = nuc_file_fullpath
					new_file_path = _des_folder+'/'+each_nuc_file
					print("new_file_path: " + new_file_path)
					json_info_dict['destination_path'] = new_file_path
					os.rename(nuc_file_fullpath, new_file_path)
					print(json_info_dict)
				jsonString = json.dumps(json_info_dict, indent=2, separators=(',', ': '))
				jsonFile.write(jsonString)
		else:
			print_header("Not folder")
		#check_individual_nuc_folder_files(_base_dir_name, each_item_folder_name)
	jsonFile.close()
def arrange_nuc_files_to_folder(knan_software_dir):
	full_item_dir_list = []
	for item in os.listdir(knan_software_dir):
		full_item_dir_list.append(os.path.join(knan_software_dir, item))
	#print_debug(full_item_dir_list)
	create_ftdi_folders_and_move_ftdi_files(full_item_dir_list, knan_software_dir)
	
def main():
	#arrange_nuc_files_to_folder("D:\py_test_KNAN_software", "D:\py_test_des_folder")
	extract_files_in_childfolders_to_des("D:\py_test_KNAN_software", "D:\py_test_des_folder")
if __name__ == "__main__":
    main()