# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json

# global vars
fullpath_src_folder = ""
underscore_index_list = []
allow_print_debug_info = 1

def print_debug(s):
	if allow_print_debug_info==1:
		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)


def check_and_change_nucfolder_name(_filepath):
	global fullpath_src_folder
	count = 1
	root_folder_ls_list = os.listdir(_filepath)
	for each_item_folder_name in root_folder_ls_list:
		valid_ftdi_flag = 0
		good_name_flag = 0
		print_header("***STT: " + str(count))
		count = count + 1
		#print(each_item_folder_name)
		fullpath_src_folder = _filepath+'/'+each_item_folder_name
		print("Full _filepath: " + fullpath_src_folder)
		# all root_folder_ls_list and folder in fullpath_src_folder
		src_folder_ls = os.listdir(fullpath_src_folder)
		underscore_index_list = find(each_item_folder_name, "_")
		underscore_count = len(underscore_index_list)
		for tb_file in src_folder_ls:
			valid_ftdi_flag, extracted_ftdi = get_full_ftdi_from_file_name(tb_file)
			if valid_ftdi_flag == 1:
				break
		# check if folder name is already good
		if valid_ftdi_flag == 1:
			if underscore_count == 0:
				# continue the for loop for this each_item_folder_name
				print_fail("Discard this for loop as no underscore found")
				continue
			if underscore_count == 1:
				new_folder_name = each_item_folder_name[0:underscore_index_list[0]+1]+extracted_ftdi
				if (len(each_item_folder_name[underscore_index_list[0]:]) == c_ftdi_length+1):
					good_name_flag = 1
			if underscore_count >= 2:
				if (underscore_index_list[1]-underscore_index_list[0] == c_ftdi_length+1):
					good_name_flag = 1
				new_folder_name = each_item_folder_name[0:underscore_index_list[0]+1]+extracted_ftdi+each_item_folder_name[underscore_index_list[1]:]
			if good_name_flag==1:
				print_ok("Discard this as the each_item_folder_name is already OK")
				continue
			new_fullpath_folder_name = _filepath+'/'+new_folder_name
			print("fullpath_src_folder: "+ fullpath_src_folder + "; new_fullpath_folder_name: " + new_fullpath_folder_name)

			# start rename
			if g_allow_rename == 1:
				try:
					os.rename(fullpath_src_folder, new_fullpath_folder_name)
					print("Folder name changed sucessfully")
				except OSError:
					print_fail("Error!")
			else:
				print("Folder name isn't change")
		else:
			print_fail("None valid FTDI file is found")

# -20, -10, 0,...
temp_file_check = array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])
check_folder_content_ok_flag = 0

# Remove string after # character
# VD: D:\Dulieu_NUC_KNAN\fromOneDrive_PC_HDD\031_FT5P10Z3_ok
def remove_original_msg(_dir_full_path):
	#global fullpath_src_folder
	first_status_index = _dir_full_path.find("#")
	#print(first_status_index)
	new_name = ""
	if first_status_index>1:
		new_name = _dir_full_path[0:first_status_index]
		print(new_name)
		rename_folder(_dir_full_path, new_name)
	return new_name

def append_checkmsg_to_folder_name(st, _dir_full_path):
	global fullpath_src_folder
	global check_folder_content_ok_flag
	new_folder_name = remove_original_msg(_dir_full_path)
	end_str = "#"
	if st == 0:
		end_str = end_str + "fcOK"
		check_folder_content_ok_flag = 1
	else:
		end_str = end_str + "fcF"
		check_folder_content_ok_flag = 0
	# start rename
	if new_folder_name=="":
		rename_folder(_dir_full_path, _dir_full_path+end_str)
	else:
		rename_folder(new_folder_name, new_folder_name+end_str)

each_item_folder_ls_list = []
# _full_dir_path = D:\Dulieu_NUC_KNAN\fromOneDrive_PC_HDD\002_FT5P16DM
# _each_item_folder_ls_list = [FT5P16DM_190521_50.bin, FT5OUSZM_310521_30.bin, Log_FT5OUSZM.txt]
def get_ftdi_and_check_all_files(_full_dir_path, _each_item_folder_ls_list):
	done_get_ftdi_flag = 0
	ok_temp_file_count = 0
	ok_generated_file_count = 0
	ok_log_file_count = 0
	# tb_file: FT5P16DM_190521_50.bin
	for tb_file in _each_item_folder_ls_list:
		file_type = -1
		if done_get_ftdi_flag == 0:
			get_ftdi_status, extracted_ftdi = get_full_ftdi_from_file_name(tb_file)
			if get_ftdi_status==1:
				done_get_ftdi_flag = 1
		if done_get_ftdi_flag == 1:
			file_type = check_file_name_and_size(tb_file, get_file_size(_full_dir_path+'/'+tb_file))
			if file_type==1:
				ok_temp_file_count = ok_temp_file_count + 1
			elif file_type==2:
				ok_generated_file_count = ok_generated_file_count + 1
			elif file_type==3:
				ok_log_file_count = ok_log_file_count + 1
	error_st = print_check_file_content_message(ok_temp_file_count, ok_generated_file_count, ok_log_file_count)
	append_checkmsg_to_folder_name(error_st, _full_dir_path)
	# append check status message to end of folder name

json_file_name = ""

# input: D:\Dulieu_NUC_KNAN\fromOneDrive_PC_HDD
def remove_status_msg_from_nuc_folder_name(_filename):
	count = 1
	root_folder_ls_list = os.listdir(_filename)
	#jsonFile = open(json_file_name, "w")
	for each_item_folder_name in root_folder_ls_list:
		print_header("***STT: " + str(count))
		count = count + 1
		fullpath_src_folder = _filename + '/' + each_item_folder_name
		print(fullpath_src_folder)
		each_item_folder_ls_list = os.listdir(fullpath_src_folder)
		each_item_folder_file_count = len(each_item_folder_ls_list)
		# check_standard_files_count(each_item_folder_file_count)
		if each_item_folder_file_count>0:
			remove_original_msg(fullpath_src_folder)
		#aDict = [{"stt": count, "foder_name": each_item_folder_name, "ma_thiet_bi": "place_holder", "ftdi_name": extracted_ftdi, "files_check_status": check_folder_content_ok_flag}]
		#jsonString = json.dumps(aDict, indent=2, separators=(',', ': '))
		#jsonString = json.dumps(aDict)
		#jsonFile.write(jsonString)
		print_header("--------------------------------------------------------------------------------------------")
	#jsonFile.close()

# RETURN LIST: [ftdi number, number of files, file name and check status,
# temperature files check status, output files check and status, Log files check and status, check result]
def check_individual_nuc_folder_files(_base_dir_name, _nuc_dir_name):
	full_dir_path = _base_dir_name + '/' + _nuc_dir_name
	print(full_dir_path)
	# all root_folder_ls_list and folder in fullpath_src_folder
	each_item_folder_ls_list = os.listdir(full_dir_path)
	each_item_folder_file_count = len(each_item_folder_ls_list)
	check_standard_files_count(each_item_folder_file_count)
	if each_item_folder_file_count>0:
		get_ftdi_and_check_all_files(full_dir_path, each_item_folder_ls_list)
	#aDict = [{"stt": count, "foder_name": each_item_folder_name, "ma_thiet_bi": "place_holder", "ftdi_name": 123, "files_check_status": check_folder_content_ok_flag}]
	#jsonString = json.dumps(aDict, indent=2, separators=(',', ': '))
	#jsonString = json.dumps(aDict)
	#jsonFile.write(jsonString)
	print_header("--------------------------------------------------------------------------------------------")

# _filename: D:\Dulieu_NUC_KNAN\fromOneDrive_PC_HDD
# root_folder_ls_list: [061_FT5OV9HL_ok, 097_FT5OUWNJ_cancheck]
def check_complete_nuc_folder(_base_dir_name):
	count = 1
	root_folder_ls_list = os.listdir(_base_dir_name)
	# each_item_folder_name: 056_FT5OV9NG_ok
	for each_item_folder_name in root_folder_ls_list:
		print_header("***STT: " + str(count))
		count = count + 1
		check_individual_nuc_folder_files(_base_dir_name, each_item_folder_name)

	#jsonFile.close()

def main_check_complete_nuc_folder(filepath):
	print("Hello World!")
	global json_file_name
	#filePath = '/home/somedir/Documents/python/logs'
	get_datetime_string()
	json_file_name = "log_"+get_datetime_string()+".json"
	if os.path.exists(json_file_name):
		os.remove(json_file_name)
		print_ok("Delete the file ok")
	else:
		print("Can not delete the file as it doesn't exists")
		f = open(json_file_name, 'a+')
		f.close()
	#check_and_change_nucfolder_name()
	check_complete_nuc_folder(filepath)
	#readjsonfile = open(json_file_name, "r")
	#jsondata = json.load(readjsonfile)
	#print(jsondata)

def main_check_and_change_nucfolder_name(filepath):
	print("Hello World!")
	check_and_change_nucfolder_name(filepath)

def main():
	print("Hello World!")
	#main_check_complete_nuc_folder()

if __name__ == "__main__":
    main()