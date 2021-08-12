# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json

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
			print("Not a folder, skip...")

def extract_and_save_nuc_folder_info_to_json_file(_full_parent_dir, _json_file_name):
	print_debug("In function: extract_and_save_nuc_folder_info_to_json_file")
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
	#print("ftdi_dev_list:")
	#print_debug(str(ftdi_dev_list))
	# read the json file and 
	count = 0
	for folder_name in os.listdir(_full_parent_dir):
		count = count + 1
		print_header("***STT: " + str(count))
		full_dir_path = os.path.join(_full_parent_dir, folder_name)
		print(full_dir_path)
		if os.path.isdir(full_dir_path) == True:
			[idx, new_ftdi] = get_full_ftdi_from_string(folder_name)
			if idx!=-1:
				dev_serial = folder_name[0:idx].replace("_","")
				dev_serial = dev_serial.replace(" ","")
				new_user_msg = folder_name[idx+c_ftdi_length:]
				#new_user_msg = remove_original_app_msg(new_user_msg, 0)
				#print("Extracted user message: " + new_user_msg)
				
				if dev_serial.isnumeric():
					dev_serial = int(dev_serial)
					match_dict = read_and_get_match_dict_by_devserial_in_json_file(_json_file_name, dev_serial)
					if match_dict == -1:
						#if dev_serial.isnumeric():
						#print(dev_serial)
						json_info_dict = {}
						json_info_dict['dev_serial'] = dev_serial
						json_info_dict['FTDI'] = new_ftdi
						json_info_dict['msg'] = new_user_msg
						print_debug("Extracted dict from folder: " + folder_name)
						print(json_info_dict)
						ftdi_dev_list.append(json_info_dict)
					else:
						print_warning("The dictionary already exists in list, check and update current dictionary")
						index = next((i for i, item in enumerate(dict_lists) if item["dev_serial"] == dev_serial), None)
						print("index: " + str(index))
						print_debug("Found dict by dev serial: " + str(dev_serial))
						print(ftdi_dev_list[index])
						
						if match_dict["FTDI"] == new_ftdi:
							print_debug("Match FTDI")
						else:
							print_debug("Different FTDI, updating:...")
							dict_lists[index]["FTDI"] = new_ftdi
						if match_dict["msg"] == new_user_msg:
							print_debug("Match user msg")
						else:
							print_debug("Different user msg, updating:...")	
							dict_lists[index]["msg"] = new_user_msg				
		else:
			print("Not a folder, skip...")
	#print(ftdi_dev_list)
	jsonFile = open(_json_file_name, "w")
	jsonString = json.dumps(ftdi_dev_list, indent=2, separators=(',', ': '))
	jsonFile.write(jsonString)
	jsonFile.close()

def main():
	print("nuc_production")

if __name__ == "__main__":
    main()