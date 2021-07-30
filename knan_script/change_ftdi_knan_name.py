# todo: Check folder content
import os
import sys
from array import *
from utils import *
import json

# define constant
c_ftdi_length = 8
c_temperatire_file_size = 157286400
c_machine_type = 1 # 0 for ubuntu (windows subsystem for windows), 1 for windows

if c_machine_type == 0:
	#g_folder_path = '/mnt/e/du lieu nuc knan '
	g_folder_path = '/mnt/d/Dulieu_NUC_KNAN/HDD_1TB_29July21'
else:
	g_folder_path = "D:\Dulieu_NUC_KNAN\HDD_1TB_29July21"

# global vars
extracted_ftdi = ""
fullpath_src_folder = ""
underscore_index_list = []
allow_print_debug_info = 0
g_allow_rename = 1

def print_debug(s):
	if allow_print_debug_info==1:
		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)

# print to screen if all checks are ok
item_info_sring = ""
def check_and_change_nucfolder_name():
	global fullpath_src_folder
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(g_folder_path)
	for each_item_folder_name in root_folder_ls_list:
		valid_ftdi_flag = 0
		good_name_flag = 0
		print_header("***STT: " + str(count))
		count = count + 1
		#print(each_item_folder_name)
		fullpath_src_folder = g_folder_path+'/'+each_item_folder_name
		print("Full g_folder_path: " + fullpath_src_folder)
		# all root_folder_ls_list and folder in fullpath_src_folder
		src_folder_ls = os.listdir(fullpath_src_folder)
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
			new_fullpath_folder_name = g_folder_path+'/'+new_folder_name
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

# The file can be Log_FTDI.txt or matlab file
def get_full_ftdi_from_file_name(file_name):
	global extracted_ftdi
	ft_first_index = file_name.find("FT")
	if ft_first_index>=0:
		extracted_ftdi = file_name[ft_first_index:ft_first_index+c_ftdi_length]
		print_ok("FTDI: "+ extracted_ftdi)
		return 1
	else:
		extracted_ftdi = ""
		print_fail("No FTDI string in file is found!, Please check folder content!")
		return 0

# -20, -10, 0,...
temp_file_check = array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0])

def get_file_size(_file_name):
	file_fullpath = fullpath_src_folder + '/' + _file_name
	print_debug(file_fullpath)
	if os.path.exists(file_fullpath)==True:
		file_size = os.path.getsize(file_fullpath)
		print_debug("File size = " + str(file_size))
		return file_size


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

def remove_original_msg():
	global fullpath_src_folder
	first_status_index = fullpath_src_folder.find("#")
	print(first_status_index)
	new_name = ""
	if first_status_index>1:
		new_name = fullpath_src_folder[0:first_status_index]
		print(new_name)
		rename_folder(fullpath_src_folder, new_name)
	return new_name

def append_checkmsg_to_folder_name(st):
	global fullpath_src_folder
	global check_folder_content_ok_flag
	new_folder_name = remove_original_msg()
	end_str = "#"
	if st == 0:
		end_str = end_str + "fcOK"
		check_folder_content_ok_flag = 1
	else:
		end_str = end_str + "fcF"
		check_folder_content_ok_flag = 0
	# start rename
	if new_folder_name=="":
		rename_folder(fullpath_src_folder, fullpath_src_folder+end_str)
	else:
		rename_folder(new_folder_name, new_folder_name+end_str)

each_item_folder_ls_list = []

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
			if file_type==1:
				ok_temp_file_count = ok_temp_file_count + 1
			elif file_type==2:
				ok_generated_file_count = ok_generated_file_count + 1
			elif file_type==3:
				ok_log_file_count = ok_log_file_count + 1
	error_st = print_check_file_content_message()
	append_checkmsg_to_folder_name(error_st)
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
def check_complete_nuc_folder():
	global fullpath_src_folder
	global each_item_folder_ls_list
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(g_folder_path)
	jsonFile = open(json_file_name, "w")
	for each_item_folder_name in root_folder_ls_list:
		item_info_sring = ""
		print_header("***STT: " + str(count))
		count = count + 1
		fullpath_src_folder = g_folder_path + '/' + each_item_folder_name
		print(fullpath_src_folder)
		add_item_info_string("Folder full g_folder_path: " + fullpath_src_folder) 
		# all root_folder_ls_list and folder in fullpath_src_folder
		each_item_folder_ls_list = os.listdir(fullpath_src_folder)
		each_item_folder_file_count = len(each_item_folder_ls_list)
		check_file_count(each_item_folder_file_count)
		if each_item_folder_file_count>0:
			get_ftdi_and_check_all_files()
		print(item_info_sring)
		aDict = [{"stt": count, "foder_name": each_item_folder_name, "ma_thiet_bi": "place_holder", "ftdi_name": extracted_ftdi, "files_check_status": check_folder_content_ok_flag}]
		jsonString = json.dumps(aDict, indent=2, separators=(',', ': '))
		#jsonString = json.dumps(aDict)
		jsonFile.write(jsonString)
		
		print_header("--------------------------------------------------------------------------------------------")
	jsonFile.close()

def main_check_complete_nuc_folder():
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
	check_complete_nuc_folder()
	#readjsonfile = open(json_file_name, "r")
	#jsondata = json.load(readjsonfile)
	#print(jsondata)

def main_check_and_change_nucfolder_name():
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
	check_and_change_nucfolder_name()
	#readjsonfile = open(json_file_name, "r")
	#jsondata = json.load(readjsonfile)
	#print(jsondata)

def main():
	main_check_complete_nuc_folder()

if __name__ == "__main__":
    main()