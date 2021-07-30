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
# path = '/mnt/d/Dulieu_NUC_KNAN/HDD_1TB_29July21'

# extracted_ftdi = ""

# ftdi_length = 8
# fullpath_src_folder = ""
# underscore_index_list = []
# allow_print_debug_info = 1
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

# def print_debug(s):
# 	if allow_print_debug_info==1:
# 		print(bcolors.OKBLUE + "Db: " + s + bcolors.ENDC)
# print to screen if all checks are ok
#item_info_sring = ""
