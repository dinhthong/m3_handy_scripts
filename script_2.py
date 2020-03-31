#https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value-python-3-6/51801421
from openpyxl import Workbook
import openpyxl
print("Hello world")
file = "./../thong_dmvt_lo1048/file_goc/EBOM_VEE-B01_Lan 11_Kien.xlsx"
wb = openpyxl.load_workbook(file, read_only=True)
#print(wb.sheetnames)
# Select a specific sheet to work
ws = wb["PL6_BOM_machchinh"]
ma_nsx_list = []
# iterate every row in column 
i = 1
wb_first_row = 14
wb_last_row = 147
for row in ws.iter_rows("I"):
    for cell in row:
        # limit to the rows where Ma NSX are available
        # note that some cases we must manually link in order to complete an Excel sheet. 
        if i>=wb_first_row and i<=wb_last_row:
            ma_nsx_list.append([i,cell.value])
            #print(cell.value)
        # increase row index
        i = i+1
print("There're total of " + str(wb_last_row-wb_first_row+1) + " component to be map the new SAP B1 component code")
# print the list contain all ma nxs to map to target file along with its row index in previous file to Danh muc vat tu LINH KIEN.xlsx
#print(ma_nsx_list)
file1 = "./../thong_dmvt_lo1048/file_goc/Danh muc vat tu LINH KIEN.xlsx"
component_code_match_row_index = 1
wb1 = openpyxl.load_workbook(file1, read_only=True)
ws1 = wb1.active
print(wb1.sheetnames) 
print(len(ma_nsx_list))
# search each item in ma_nsx_list in every row of column C (Ky ma hieu) in `Danh muc vat tu LINH KIEN.xlsx`
component_code_cnt = 0
none1_cnt = 0
for item in ma_nsx_list:
    #print(item[1])
    for row in ws1.iter_rows("C"):
        for cell in row:
            # if we detect any matching by component code
            if cell.value == item[1]:
                #print("hi")
                component_code_cnt = component_code_cnt+1
                print(component_code_cnt)
                print(item[0])
                print(component_code_match_row_index)
                print(ws1.cell(None, component_code_match_row_index, 4).value)
                item.append(component_code_match_row_index)
                if ws1.cell(None, component_code_match_row_index, 4).value == None:
                    print("None value detected, we won't use this for the next code")
                    none1_cnt = none1_cnt+1
                item.append(ws1.cell(None, component_code_match_row_index, 4).value)
                print("----")

            component_code_match_row_index = component_code_match_row_index+1
        # reset the counter for next loop    
    component_code_match_row_index = 1
# STT in Excel 1, Component Code, STT in Excel 2, Ma vat tu cu
#print(ma_nsx_list)
print("Number of items matched by component code: " + str(component_code_cnt-none1_cnt)+" / "+str(wb_last_row-wb_first_row+1))
nsx_code_match_row_index = 1
file2 = "./../thong_dmvt_lo1048/file_goc/List of Items 31-03-2020.xlsx"
wb2 = openpyxl.load_workbook(file2, read_only=True)
ws2 = wb2.active
print(wb2.sheetnames)

for item in ma_nsx_list:
    for row in ws2.iter_rows("F"):
        for cell in row:
            # if we detect any matching
            #print(cell.value)
            #print(item[3])
            #print("row_index" + str(nsx_code_match_row_index))
            if cell.value == item[3]:
                #print("hi")
                print(item[0])
                print(item[1])
                print(item[2])
                print(item[3])
                #print(nsx_code_match_row_index)
                print(ws2.cell(None, nsx_code_match_row_index, 2).value)
                #item.append(component_code_match_row_index)
                if ws2.cell(None, nsx_code_match_row_index, 2).value == None:
                    print("None value detected, we won't use this for the next code")
                item.append(ws2.cell(None, nsx_code_match_row_index, 2).value)
                print("----")
            nsx_code_match_row_index = nsx_code_match_row_index+1
        # reset the counter for next loop    
    nsx_code_match_row_index = 1

print(ma_nsx_list)