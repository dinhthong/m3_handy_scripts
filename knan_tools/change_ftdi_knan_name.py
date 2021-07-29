import os
import sys

path = '/mnt/e/du lieu nuc knan '
files = os.listdir(path)
count = 1
ftdi_length = 8
rname_flag = 0
print("Hello world!")
for folder_name in files:
	valid_ftdi_flag = 0

	print("***STT: " + str(count))
	count = count + 1
	#print(folder_name)
	fullpath_src_folder = path+'/'+folder_name
	print(fullpath_src_folder)
	# all files and folder in fullpath_src_folder
	src_folder_ls = os.listdir(fullpath_src_folder)
	foldername_underscore_count = folder_name.count("_")
	
	for tb_file in src_folder_ls:
		#print(tb_file)
		# if first char of tb_file is F -> get the name then break for loop
		if tb_file[0] == 'F':
			valid_ftdi_flag = 1
			ftdi_str = tb_file[0:ftdi_length]
			# get full FTDI name
			print(ftdi_str)
			break
	# if there's 1 underscore -> 
	if valid_ftdi_flag == 1:
		if foldername_underscore_count == 1:
			# find underscore index in folder name, and concat string
			underscore_index = folder_name.index("_")
			new_folder_name = folder_name[0:underscore_index+1]+ftdi_str

			print("New folder name will be: "+new_folder_name)
			fullpath_des_folder = path+'/'+new_folder_name
			print("fullpath_src_folder: "+fullpath_src_folder+ " fullpath_des_folder: " +fullpath_des_folder)
			# start rename
			try:
				os.rename(fullpath_src_folder, fullpath_des_folder)
				print("Name changed sucessfully")
			except WindowsError:
				print("Error!")
				#os.remove(newName)
				#os.rename(f, newName)
		if foldername_underscore_count == 2:
			#replace between two first underscore with new FTDI name
	print("")
