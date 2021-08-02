# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json
import shutil

# define constant
c_ftdi_length = 8
c_temperatire_file_size = 157286400

# global vars
extracted_ftdi = ""
item_fullpath = ""
underscore_index_list = []
allow_print_debug_info = 0
g_allow_rename = 1

def print_debug(s):
	if allow_print_debug_info==1:
		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)

# print to screen if all checks are ok
item_info_sring = ""
def check_and_change_nucfolder_name(_filepath):
	global item_fullpath
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(_filepath)
	for each_item_folder_name in root_folder_ls_list:
		valid_ftdi_flag = 0
		good_name_flag = 0
		print_header("***STT: " + str(count))
		count = count + 1
		#print(each_item_folder_name)
		item_fullpath = _filepath+'/'+each_item_folder_name
		print("Full _filepath: " + item_fullpath)
		# all root_folder_ls_list and folder in item_fullpath
		src_folder_ls = os.listdir(item_fullpath)
		underscore_index_list = find(each_item_folder_name, "_")
		underscore_count = len(underscore_index_list)
		for tb_file in src_folder_ls:
			valid_ftdi_flag = get_full_ftdi_from_file_name(tb_file)
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
			print("item_fullpath: "+ item_fullpath + "; new_fullpath_folder_name: " + new_fullpath_folder_name)

			# start rename
			if g_allow_rename == 1:
				try:
					os.rename(item_fullpath, new_fullpath_folder_name)
					print("Folder name changed sucessfully")
				except OSError:
					print_fail("Error!")
			else:
				print("Folder name isn't change")
		else:
			print_fail("None valid FTDI file is found")

# The file can be Log_FTDI.txt or matlab file


# -20, -10, 0,...
temp_file_check = array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])

def check_file_name_and_size(_fname, _fsize):
	if _fname.find(".bin") != -1:
		underscore_index_list = find(_fname, "_")
		if len(underscore_index_list)==2:
			if _fsize==c_temperatire_file_size:
				print_ok("Temperature file size ok")
				return 1
			else:
				print_fail("Temperature file size NOT ok")
		else:
			print("output file")
			return 2
	elif _fname.find(".txt"):
		print("Log file detected")
		return 3

ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0

check_folder_content_ok_flag = 0

def print_check_file_content_message():
	global ok_temp_file_count
	global ok_generated_file_count
	global ok_log_file_count
	error = 0
	temp_str = "ok_temp_file_count: " + str(ok_temp_file_count)+"/9"
	if ok_temp_file_count == 9:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	temp_str = "ok_generated_file_count: " + str(ok_generated_file_count)+"/5"
	if ok_generated_file_count == 5:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	temp_str ="ok_log_file_count: " + str(ok_log_file_count)+"/1"
	if ok_log_file_count == 1:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	return error

def rename_folder(_src, _des):
	if g_allow_rename == 1:
		try:
			os.rename(_src, _des)
			print("Folder name changed sucessfully")
			print("New name: "+_des)
		except OSError:
			print_fail("Error rename, check files/folders!")
	else:
		print("Folder name isn't change")

each_item_folder_ls_list = []
# Create if not exist
def create_data_FTDI_folder(base, ftdi):
	#get_datetime_string()
	ftdi_folder_path = base + "/data_" + ftdi
	try:
		os.mkdir(ftdi_folder_path) 
	except OSError as error: 
		print(error)
	
def get_ftdi_and_check_all_files():
	global each_item_folder_ls_list
	global ok_temp_file_count
	global ok_generated_file_count
	global ok_log_file_count
	done_get_ftdi_flag = 0
	ok_temp_file_count = 0
	ok_generated_file_count = 0
	ok_log_file_count = 0
	for tb_file in each_item_folder_ls_list:
		file_type = -1
		if done_get_ftdi_flag == 0 and get_full_ftdi_from_file_name(tb_file) == 1:
			done_get_ftdi_flag = 1
		if done_get_ftdi_flag == 1:
			file_type = check_file_name_and_size(tb_file, get_file_size(tb_file))
			# if file_type==1:
			# 	ok_temp_file_count = ok_temp_file_count + 1
			# elif file_type==2:
			# 	ok_generated_file_count = ok_generated_file_count + 1
			# elif file_type==3:
			# 	ok_log_file_count = ok_log_file_count + 1
	error_st = print_check_file_content_message()
	#append_checkmsg_to_folder_name(error_st)
	# append check status message to end of folder name

def check_file_count(file_count):
	print("File count: " + str(file_count))
	if file_count == 0:
		print_fail("Folder empty!")
	else:
		if file_count == 15:
			print_ok("File count ok")
			add_item_info_string("File count ok")
		else:
			print_fail("File count error")
			add_item_info_string("File count error")

def add_item_info_string(s):
	global item_info_sring
	item_info_sring = item_info_sring + s + "\n"

def add_item_info_string_fail(s):
	global item_info_sring
	item_info_sring = item_info_sring + bcolors.WARNING + s + bcolors.ENDC + "\n"

json_file_name = ""

def create_ftdi_folders_and_move_ftdi_files(base_dir, folder_ls_list):
	count = 1
	for each_item_folder_name in folder_ls_list:
		print_header("***STT: " + str(count))
		count = count + 1
		item_fullpath = base_dir + '/' + each_item_folder_name
		print(item_fullpath)
		add_item_info_string("ITEM full _filename: " + item_fullpath) 
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
	

def remove_status_msg_from_nuc_folder_name(_filename):
	global item_fullpath
	global each_item_folder_ls_list
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(_filename)
	#jsonFile = open(json_file_name, "w")
	for each_item_folder_name in root_folder_ls_list:
		item_info_sring = ""
		print_header("***STT: " + str(count))
		count = count + 1
		item_fullpath = _filename + '/' + each_item_folder_name
		print(item_fullpath)
		add_item_info_string("Folder full _filename: " + item_fullpath) 
		# all root_folder_ls_list and folder in item_fullpath
		each_item_folder_ls_list = os.listdir(item_fullpath)
		each_item_folder_file_count = len(each_item_folder_ls_list)
		check_file_count(each_item_folder_file_count)
		if each_item_folder_file_count>0:
			remove_original_msg()
		print(item_info_sring)
		#aDict = [{"stt": count, "foder_name": each_item_folder_name, "ma_thiet_bi": "place_holder", "ftdi_name": extracted_ftdi, "files_check_status": check_folder_content_ok_flag}]
		#jsonString = json.dumps(aDict, indent=2, separators=(',', ': '))
		#jsonString = json.dumps(aDict)
		#jsonFile.write(jsonString)
		print_header("--------------------------------------------------------------------------------------------")
	#jsonFile.close()

def check_complete_nuc_folder(_filename):
	global item_fullpath
	global each_item_folder_ls_list
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(_filename)
	#jsonFile = open(json_file_name, "w")
	for each_item_folder_name in root_folder_ls_list:
		item_info_sring = ""
		print_header("***STT: " + str(count))
		count = count + 1
		item_fullpath = _filename + '/' + each_item_folder_name
		print(item_fullpath)
		add_item_info_string("Folder full _filename: " + item_fullpath) 
		# all root_folder_ls_list and folder in item_fullpath
		each_item_folder_ls_list = os.listdir(item_fullpath)
		each_item_folder_file_count = len(each_item_folder_ls_list)
		check_file_count(each_item_folder_file_count)
		if each_item_folder_file_count>0:
			get_ftdi_and_check_all_files()
		print(item_info_sring)
		aDict = [{"stt": count, "foder_name": each_item_folder_name, "ma_thiet_bi": "place_holder", "ftdi_name": extracted_ftdi, "files_check_status": check_folder_content_ok_flag}]
		jsonString = json.dumps(aDict, indent=2, separators=(',', ': '))
		#jsonString = json.dumps(aDict)
		#jsonFile.write(jsonString)
		print_header("--------------------------------------------------------------------------------------------")
	#jsonFile.close()

def main_check_complete_nuc_folder(filepath):
	print("Hello World!")
	#global json_file_name
	#filePath = '/home/somedir/Documents/python/logs'
	get_datetime_string()
	#json_file_name = "log_"+get_datetime_string()+".json"
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
	# global json_file_name
	#filePath = '/home/somedir/Documents/python/logs'
	# get_datetime_string()
	# json_file_name = "log_"+get_datetime_string()+".json"
	# if os.path.exists(json_file_name):
	# 	os.remove(json_file_name)
	# 	print_ok("Delete the file ok")
	# else:
	# 	print("Can not delete the file as it doesn't exists")
	# 	f = open(json_file_name, 'a+')
	# 	f.close()
	check_and_change_nucfolder_name(filepath)
	#readjsonfile = open(json_file_name, "r")
	#jsondata = json.load(readjsonfile)
	#print(jsondata)

def main():
	#main_check_complete_nuc_folder()
	copy_from_nuc_data_folder_to_des("D:\py_test_KNAN_software", "D:\py_test_des_folder")
if __name__ == "__main__":
    main()