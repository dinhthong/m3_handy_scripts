# todo: Check folder content
import os
import sys
from array import *
from datetime import date
from datetime import datetime

# define constant
c_ftdi_length = 8
c_temperatire_file_size = 157286400

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

def get_datetime_string():
	now = date.today()
	current_date = now.strftime("%Y_%m_%d")
	#print_debug("Today's date:", current_date)
	now = datetime.now()
	current_time = now.strftime("%H_%M_%S")
	#print("Current Time =", current_time)
	date_time_str = current_date+"T"+current_time
	#print(date_time_str)
	return date_time_str

def get_full_ftdi_from_file_name(file_name):
	ft_first_index = file_name.find("FT")
	return_status = 0
	if ft_first_index>=0:
		get_ftdi = file_name[ft_first_index:ft_first_index+c_ftdi_length]
		print_ok("FTDI: "+ get_ftdi)
		return_status = 1
	else:
		get_ftdi = ""
		print_fail("No FTDI string in file is found!, Please check folder content!")
		return_status = 0
	return return_status, get_ftdi

def get_file_size(_file_fullpath):
	#file_fullpath = fullpath_src_folder + '/' + _fullpath_file
	print("Get file size: "+_file_fullpath)
	if os.path.exists(_file_fullpath)==True and os.path.isfile(_file_fullpath) == True:
		file_size = os.path.getsize(_file_fullpath)
		print_ok("File size = " + str(file_size))
		return file_size
	else:
		print_fail("Can't get file size")
		return -1

def print_check_file_content_message(_ok_temp_file_count, _ok_generated_file_count, _ok_log_file_count):
	error = 0
	temp_str = "_ok_temp_file_count: " + str(_ok_temp_file_count)+"/9"
	if _ok_temp_file_count == 9:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	temp_str = "_ok_generated_file_count: " + str(_ok_generated_file_count)+"/5"
	if _ok_generated_file_count == 5:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	temp_str ="_ok_log_file_count: " + str(_ok_log_file_count)+"/1"
	if _ok_log_file_count == 1:
		print_ok(temp_str)
	else:
		print_fail(temp_str)
		error = error + 1
	return error

def check_standard_files_count(file_count):
	print("File count: " + str(file_count))
	if file_count == 0:
		print_fail("Folder empty!")
	else:
		if file_count == 15:
			print_ok("File count ok")
			# add_item_info_string("File count ok")
		else:
			print_fail("File count error")
			# add_item_info_string("File count error")