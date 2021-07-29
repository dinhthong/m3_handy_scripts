# todo: Check folder content
import os
import sys
from array import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#path = '/mnt/e/du lieu nuc knan '
path = '/mnt/d/Dulieu_NUC_KNAN/HDD_1TB_29July21'

extracted_ftdi = ""

ftdi_length = 8
fullpath_src_folder = ""
underscore_index_list = []
allow_print_debug_info = 1
#https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def print_header(s):
	print(bcolors.HEADER + s + bcolors.ENDC)

def print_warning(s):
	print(bcolors.WARNING + s + bcolors.ENDC)

def print_fail(s):
	print(bcolors.FAIL + s + bcolors.ENDC)
def print_ok(s):
	print(bcolors.OKCYAN + s + bcolors.ENDC)

def print_debug(s):
	if allow_print_debug_info==1:
		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)
# print to screen if all checks are ok
item_info_sring = ""
def check_and_change_nucfolder_name(do_change_flag):
	global fullpath_src_folder
	global extracted_ftdi
	count = 1
	root_folder_ls_list = os.listdir(path)
	for each_item_folder_name in root_folder_ls_list:
		valid_ftdi_flag = 0
		good_name_flag = 0
		print_header("***STT: " + str(count))
		count = count + 1
		#print(each_item_folder_name)
		fullpath_src_folder = path+'/'+each_item_folder_name
		print("Full path: " + fullpath_src_folder)
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
				if (len(each_item_folder_name[underscore_index_list[0]:]) == ftdi_length+1):
					good_name_flag = 1
			if underscore_count >= 2:
				if (underscore_index_list[1]-underscore_index_list[0] == ftdi_length+1):
					good_name_flag = 1
				new_folder_name = each_item_folder_name[0:underscore_index_list[0]+1]+extracted_ftdi+each_item_folder_name[underscore_index_list[1]:]
			if good_name_flag==1:
				print_ok("Discard this as the each_item_folder_name is already OK")
				continue
			new_fullpath_folder_name = path+'/'+new_folder_name
			print("fullpath_src_folder: "+ fullpath_src_folder + "; new_fullpath_folder_name: " + new_fullpath_folder_name)

			# start rename
			if do_change_flag == 1:
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
		extracted_ftdi = file_name[ft_first_index:ft_first_index+ftdi_length]
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

tepm_file_size = 157286400
def check_file_name_and_size(_fname, _fsize):
	if _fname.find(".bin") != -1:
		underscore_index_list = find(_fname, "_")
		if len(underscore_index_list)==2:
			if _fsize==tepm_file_size:
				print_ok("Temperature file ok")
				return 1
			else:
				print_fail("Temperature file NOT ok")
		else:
			print("output file")
			return 2
	elif _fname.find(".txt"):
		print("Log file detected")
		return 3

ok_temp_file_count = 0
ok_generated_file_count = 0
ok_log_file_count = 0

def print_check_file_content_message():
	global ok_temp_file_count
	global ok_generated_file_count
	global ok_log_file_count

	temp_str = "ok_temp_file_count: " + str(ok_temp_file_count)+"/9"
	if ok_temp_file_count == 9:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
	temp_str = "ok_generated_file_count: " + str(ok_generated_file_count)+"/5"
	if ok_generated_file_count == 5:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
	temp_str ="ok_log_file_count: " + str(ok_log_file_count)+"/1"
	if ok_log_file_count == 1:
		print_ok(temp_str)
	else:
		print_fail(temp_str)


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
	print_check_file_content_message()
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

def check_complete_nuc_folder():
	global fullpath_src_folder
	global each_item_folder_ls_list
	count = 1
	root_folder_ls_list = os.listdir(path)
	for each_item_folder_name in root_folder_ls_list:
		item_info_sring = ""
		print_header("***STT: " + str(count))
		count = count + 1
		fullpath_src_folder = path + '/' + each_item_folder_name
		print(fullpath_src_folder)
		add_item_info_string("Folder full path: " + fullpath_src_folder) 
		# all root_folder_ls_list and folder in fullpath_src_folder
		each_item_folder_ls_list = os.listdir(fullpath_src_folder)
		each_item_folder_file_count = len(each_item_folder_ls_list)
		check_file_count(each_item_folder_file_count)
		if each_item_folder_file_count>0:
			get_ftdi_and_check_all_files()
		print(item_info_sring)
		print_header("--------------------------------------------------------------------------------------------")
	
def main():
	print("Hello World!")
	#check_and_change_nucfolder_name(0)
	check_complete_nuc_folder()
if __name__ == "__main__":
    main()