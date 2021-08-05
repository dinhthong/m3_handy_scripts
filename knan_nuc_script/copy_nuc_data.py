# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json
import shutil

# define constant
c_ftdi_length = 8
# -20, -10, 0,...
ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0

check_folder_content_ok_flag = 0
json_file_name = ""

# _paren_folder: D:\py_test_KNAN_software
def extract_files_in_childfolders_to_des(_paren_folder, _des_folder):
	root_folder_ls_list = os.listdir(_paren_folder)
	# each_item_folder_name: 056_FT5OV9NG_ok
	jfilename= get_json_file_name()
	jsonFile = open(jfilename, "w")
	for each_item_folder_name in root_folder_ls_list:
		nuc_folder_fullpath = os.path.join(_paren_folder, each_item_folder_name)
		if os.path.isdir(nuc_folder_fullpath) == True:
			nuc_folder_fullpath_ls = os.listdir(nuc_folder_fullpath)
			count = 0
			for each_nuc_file in nuc_folder_fullpath_ls:
				json_info_dict = {}
				count = count + 1
				print_header("***STT: " + str(count))
				json_info_dict['STT'] = count
				nuc_file_fullpath = os.path.join(nuc_folder_fullpath, each_nuc_file)
				print(nuc_file_fullpath)
				if check_temperature_file(nuc_file_fullpath) == True:
					#json_info_dict['md5'] = get_md5_hash(nuc_file_fullpath)
					print("nuc_file_fullpath: " + nuc_file_fullpath)
					json_info_dict['original_path'] = nuc_file_fullpath
					new_file_path = os.path.join(_des_folder, each_nuc_file)
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
	print("copy_nuc_data")
	# arrange_nuc_files_to_folder("D:\py_test_KNAN_software", "D:\py_test_des_folder")
	# extract_files_in_childfolders_to_des("D:\py_test_KNAN_software", "D:\py_test_des_folder")

if __name__ == "__main__":
    main()