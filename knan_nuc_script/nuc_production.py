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
ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0
check_folder_content_ok_flag = 0
# Create if not exist
def create_data_FTDI_folder(base, ftdi):
	#get_datetime_string()
	ftdi_folder_path = base + "/data_" + ftdi
	try:
		os.mkdir(ftdi_folder_path) 
	except OSError as error: 
		print(error)

# arrange in level 1 subfolders
def arrange_nuc_files_in_firstlevel_subfolder(full_parent_dir):
	for item in os.listdir(full_parent_dir):
		full_dir_path = os.path.join(full_parent_dir, item)
		if os.path.isdir(full_dir_path) == True:
			print(full_dir_path)
			full_item_dir_list = []
			for item in os.listdir(full_dir_path):
				full_item_dir_list.append(os.path.join(full_dir_path, item))
			create_ftdi_folders_and_move_ftdi_files(full_item_dir_list, full_parent_dir)
		else:
			print("Not a folder, dissmiss")

# iterate all folders
# detect and get FTDI first index: n
# strip folder name from index 0 to n, check if it's a valid number
# create a device and FTDI pair, with dev serial as primary key.
# for each dev serial, if the pair value doesn't change, skip
# if it changes, ->

def get_and_save_ftdi_devserial_pair(_full_parent_dir, _json_file_name):
	# read the current json file and save to list
	if os.path.isfile(_json_file_name):
		f = open(_json_file_name, "r")
	else:
		print("File doesn't exist")
		f = open(_json_file_name, 'a+')

	# returns JSON object as 
	# a dictionary
	try:
		dict_lists = json.load(f)
	except:
		dict_lists = []
	f.close()
	ftdi_dev_list = dict_lists
	print("ftdi_dev_list:")
	print_debug(str(ftdi_dev_list))
	# read the json file and 
	count = 0
	for folder_name in os.listdir(_full_parent_dir):
		count = count + 1
		print_header("***STT: " + str(count))
		full_dir_path = os.path.join(_full_parent_dir, folder_name)
		print(full_dir_path)
		if os.path.isdir(full_dir_path) == True:
			[idx, ftdi] = get_full_ftdi_from_string(folder_name)
			if idx!=-1:
				#if 
				user_msg = folder_name[idx+c_ftdi_length:]
				#user_msg = remove_original_app_msg(user_msg, 0)
				print("Extracted user message: " + user_msg)
				list_or_negativeone = read_and_get_devserial_from_ftdi_in_json_file(_json_file_name, ftdi)
				# print("Return value for read_and_get_devserial_from_ftdi_in_json_file(), in get_and_save_ftdi_devserial_pair):" + str(r))
				# if the pair doesn't exist in current json file -> add new dictonary pair to the list
				if list_or_negativeone==-1:
					#print(stt)
					#print(folder_name[0:idx])
					dev_serial = folder_name[0:idx].replace("_","")
					dev_serial = dev_serial.replace(" ","")
					if dev_serial.isnumeric():
						#print(dev_serial)
						json_info_dict = {}
						json_info_dict['dev_serial'] = int(dev_serial)
						json_info_dict['FTDI'] = ftdi
						json_info_dict['msg'] = user_msg
						print(json_info_dict)
						ftdi_dev_list.append(json_info_dict)
				else:
					print_fail("The dictionary already exists in list, skip adding to JSON file")
		else:
			print("Not a folder, skip...")
	jsonFile = open(_json_file_name, "w")
	jsonString = json.dumps(ftdi_dev_list, indent=2, separators=(',', ': '))
	jsonFile.write(jsonString)
	jsonFile.close()

def main():
	print("nuc_production")
	# arrange_nuc_files_to_folder("D:\py_test_KNAN_software", "D:\py_test_des_folder")
	# arrange_nuc_files_in_firstlevel_subfolder("D:\py_test_KNAN_software", "D:")
	# get_and_save_ftdi_devserial_pair("D:\\Dulieu_NUC_KNAN\\fromOneDrive_PC_HDD", jfilename)
	#get_ftdi = read_and_get_devserial_from_ftdi_in_json_file(jfilename, "2FT5OUTLD")
	#print("get_ftdi: " + str(get_ftdi))
if __name__ == "__main__":
    main()