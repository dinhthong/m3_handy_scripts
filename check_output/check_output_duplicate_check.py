#!/usr/bin/python

#https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value-python-3-6/51801421
# component_code_list = [STT in Excel 1, Component Code, STT in Excel 2, Ma vat tu cu]
# first excel sheet name
# wb range for first sheet
#
from openpyxl import Workbook
import openpyxl

print("Check output SAP B1 auto tool for TSAN")

# FIRST EXCEL FILE
excel_path_suffix = "./../thong_dmvt_lo1048/file_goc/"

file = excel_path_suffix + "PL02, PL03_VTLK (Xong theo Ebom 11 du kien)_v3.1_script.xlsx"
new_bom_wb = openpyxl.load_workbook(file)

# USER DEFINES
# Select a specific sheet to work
new_bom_sheet = "VTLK Thau"
# Select the linking column 
file0_linking_col = "C"
# limit to the rows where Component code are available 
# (we don't handle the first info rows in the excel sheet because it's kind of time-consuming for now)
wb_first_row = 1
wb_last_row = 163

# Print information
ws = new_bom_wb[new_bom_sheet]
print("Opening excel file: " + str(file))
print("Working with excel sheet: " + str(ws))
# PROGRAMMING VARIABLES
# iterate every row in column variable
i = 1
component_code_list = []
component_code_list2 = []

def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

for row in ws.iter_rows(file0_linking_col):
    for cell in row:
        # note that some cases we must manually link in order to complete an Excel sheet. 
        if i>=wb_first_row and i<=wb_last_row:
            component_code_list.append([i,cell.value])
            component_code_list2.append(cell.value)
        i = i+1
print(len(component_code_list2))
print(component_code_list2)
#for item in component_code_list:

#for item 
result = checkIfDuplicates_2(component_code_list2)
 
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')    

print("Finish excel mapping automation tool")

