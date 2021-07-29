# todo: Check folder content
import os
import sys

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
files = os.listdir(path)
ftdi_length = 8

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
	print(bcolors.OKBLUE + s + bcolors.ENDC)

fullpath_src_folder = ""

def check_and_change_nucfolder_name(do_change_flag):
	global fullpath_src_folder
	count = 1
	for folder_name in files:
		valid_ftdi_flag = 0
		good_name_flag = 0
		print_header("***STT: " + str(count))
		count = count + 1
		#print(folder_name)
		fullpath_src_folder = path+'/'+folder_name
		print(fullpath_src_folder)
		# all files and folder in fullpath_src_folder
		src_folder_ls = os.listdir(fullpath_src_folder)
		underscore_index_list = find(folder_name, "_")
		underscore_count = len(underscore_index_list)
		for tb_file in src_folder_ls:
			# if first char of tb_file is F -> get the name then break for loop
			if tb_file[0] == 'F':
				valid_ftdi_flag = 1
				ftdi_str = tb_file[0:ftdi_length]
				# get full FTDI name
				print(ftdi_str)
				break

		# check if folder name is already good

		if valid_ftdi_flag == 1:
			if underscore_count == 0:
				# continue the for loop for this folder_name
				print_fail("Discard this for loop as no underscore found")
				continue
			if underscore_count == 1:
				new_folder_name = folder_name[0:underscore_index_list[0]+1]+ftdi_str
				if (len(folder_name[underscore_index_list[0]:]) == ftdi_length+1):
					good_name_flag = 1
			if underscore_count >= 2:
				if (underscore_index_list[1]-underscore_index_list[0] == ftdi_length+1):
					good_name_flag = 1
				new_folder_name = folder_name[0:underscore_index_list[0]+1]+ftdi_str+folder_name[underscore_index_list[1]:]
			if good_name_flag==1:
				print("Discard this as the folder_name is already OK")
				continue
			new_fullpath_folder_name = path+'/'+new_folder_name
			print("fullpath_src_folder: "+ fullpath_src_folder + "; new_fullpath_folder_name: " +new_fullpath_folder_name)

			# start rename
			if do_change_flag == 1:
				try:
					os.rename(fullpath_src_folder, new_fullpath_folder_name)
					print("Folder name changed sucessfully")
				except OSError:
					print_fail("Error!")
					#os.remove(newName)
					#os.rename(f, newName)
			else:
				print("Folder name isn't change")
		else:
			print_fail("None valid FTDI file is found")

def check_file_name_and_size(_folder_content_ls):
	global fullpath_src_folder
	for tb_file in _folder_content_ls:
		# if first char of tb_file is F -> get FTDI then break for loop
		if tb_file[0] == 'F':
			valid_ftdi_flag = 1
			ftdi_str = tb_file[0:ftdi_length]
			print(ftdi_str)
			# break for tb_file in folder_content_ls:
			break

def check_file_count(file_count, folder_content_ls):
	print("File count: " + str(file_count))
	if file_count == 0:
		print_fail("Folder empty!")
	else:
		if file_count == 15:
			print_ok("File count ok")
		else:
			print_fail("File count error")
		check_file_name_and_size(folder_content_ls)

def check_complete_nuc_folder():
	global fullpath_src_folder
	count = 1
	for folder_name in files:
		print_header("***STT: " + str(count))
		count = count + 1
		fullpath_src_folder = path+'/'+folder_name
		print(fullpath_src_folder)
		# all files and folder in fullpath_src_folder
		src_folder_ls = os.listdir(fullpath_src_folder)
		src_folder_ls_count = len(src_folder_ls)
		check_file_count(src_folder_ls_count, src_folder_ls)



def main():
	print("Hello World!")
	#check_and_change_nucfolder_name(0)
	check_complete_nuc_folder()
if __name__ == "__main__":
    main()