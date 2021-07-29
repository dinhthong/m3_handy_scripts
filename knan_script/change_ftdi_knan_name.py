import os
import sys

path = '/mnt/e/du lieu nuc knan '
files = os.listdir(path)
count = 1
ftdi_length = 8
rname_flag = 0
print("Hello world!")

#https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

for folder_name in files:
	valid_ftdi_flag = 0

	print("***STT: " + str(count))
	count = count + 1
	#print(folder_name)
	fullpath_src_folder = path+'/'+folder_name
	print(fullpath_src_folder)
	# all files and folder in fullpath_src_folder
	src_folder_ls = os.listdir(fullpath_src_folder)
	underscore_index_list = find(folder_name, "_")
	underscore_count = len(underscore_index_list)
	
	for tb_file in src_folder_ls:
		#print(tb_file)
		# if first char of tb_file is F -> get the name then break for loop
		if tb_file[0] == 'F':
			valid_ftdi_flag = 1
			ftdi_str = tb_file[0:ftdi_length]
			# get full FTDI name
			print(ftdi_str)
			break

	if valid_ftdi_flag == 1:
		if underscore_count == 0:
			# continue the for loop for this folder_name
			print("Discard this for loop as no underscore or FTDI is found")
			continue
		if underscore_count == 1:
			new_folder_name = folder_name[0:underscore_index_list[0]+1]+ftdi_str
		if underscore_count >= 2:
			new_folder_name = folder_name[0:underscore_index_list[0]+1]+ftdi_str+folder_name[underscore_index_list[1]:]
		new_fullpath_folder_name = path+'/'+new_folder_name
		print("fullpath_src_folder: "+ fullpath_src_folder + "; new_fullpath_folder_name: " +new_fullpath_folder_name)

		# start rename
		try:
			os.rename(fullpath_src_folder, new_fullpath_folder_name)
			print("Name changed sucessfully")
		except WindowsError:
			print("Error!")
			#os.remove(newName)
			#os.rename(f, newName)
	else:
		print("No valid FTDI file is found")
	print("")
