#https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value-python-3-6/51801421
# component_code_list = [STT in Excel 1, Component Code, STT in Excel 2, Ma vat tu cu]
# first excel sheet name
# wb range for first sheet
#
from openpyxl import Workbook
import openpyxl
print("SAP B1 auto tool for TSAN")
excel_path_suffix = "./../thong_dmvt_lo1048/file_goc/"
file = excel_path_suffix + "PL02, PL03_VTLK (Xong theo Ebom 11 dukien)_script.xlsx"
new_bom_wb = openpyxl.load_workbook(file)
#print(new_bom_wb.sheetnames)
# Select a specific sheet to work
new_bom_sheet = "VTLK Thau"
ws = new_bom_wb[new_bom_sheet]
component_code_list = []
# iterate every row in column variable
i = 1
# limit to the rows where Ma NSX1 are available
wb_first_row = 3
wb_last_row = 169
for row in ws.iter_rows("H"):
    for cell in row:
        # note that some cases we must manually link in order to complete an Excel sheet. 
        if i>=wb_first_row and i<=wb_last_row:
            component_code_list.append([i,cell.value])
        i = i+1
print("There're total of " + str(wb_last_row-wb_first_row+1) + " component to be map the new SAP B1 component code")
# print the list contain all ma nxs to map to target file along with its row index in previous file to Danh muc vat tu LINH KIEN.xlsx

file1 = excel_path_suffix + "Danh muc vat tu LINH KIEN.xlsx"
component_code_match_row_index = 1
wb1 = openpyxl.load_workbook(file1, read_only=True)
ws1 = wb1.active
print(wb1.sheetnames) 
print(len(component_code_list))
# search each item in component_code_list in every row of column C (Ky ma hieu) in `Danh muc vat tu LINH KIEN.xlsx`
# counter the number of original component to be searched
component_code_cnt = 0
none1_cnt = 0

list_has_foreign_name = []
for item in component_code_list:
    #print(item[1])
    for row in ws1.iter_rows("C"):
        for cell in row:
            # if we detect any matching by component code
            if cell.value == item[1]:
                component_code_cnt = component_code_cnt+1
                print("STT in first file: " + str(item[0]))
                print("Component code (Ma NXS1): " + str(item[1]))
                print("STT in second file: "+ str(component_code_match_row_index))
                
               # print(component_code_match_row_index)
                print("Foreign Name (Ma cu): " + str(ws1.cell(None, component_code_match_row_index, 4).value))
                item.append(component_code_match_row_index)
                item.append(ws1.cell(None, component_code_match_row_index, 4).value)
                if ws1.cell(None, component_code_match_row_index, 4).value == None:
                    print("None value detected, we won't use this for the next code")
                    none1_cnt = none1_cnt+1
                else:
                    list_has_foreign_name.append(item)
                print("----")

            component_code_match_row_index = component_code_match_row_index+1
        # reset the counter for next loop    
    component_code_match_row_index = 1

print("Number of items matched by component code: " + str(component_code_cnt-none1_cnt) + " / " + str(wb_last_row-wb_first_row+1))
nsx_code_match_row_index = 1
file2 = excel_path_suffix + "List of Items 31-03-2020.xlsx"
wb2 = openpyxl.load_workbook(file2, read_only=True)
ws2 = wb2.active
print(wb2.sheetnames)

for item in list_has_foreign_name:
    for row in ws2.iter_rows("F"):
        for cell in row:
            if cell.value == item[3]:
                #print(item[0])
                #print("Component code (Ma NXS1): " + str(item[1]))
                # print(item[2])
                # print("Foreign Name (Ma cu): " + str(item[3]))
                # print(nsx_code_match_row_index)
                # print("Item No. (Ma moi): " + str(ws2.cell(None, nsx_code_match_row_index, 2).value))
                if ws2.cell(None, nsx_code_match_row_index, 2).value == None:
                    print("None value detected, we won't use this for the next code")
                # STT in third excel
                item.append(nsx_code_match_row_index)
                item.append(ws2.cell(None, nsx_code_match_row_index, 2).value)
                # Ma cu
                ws.cell(row=item[0], column=5).value = item[3]
                # Ma moi
                ws.cell(row=item[0], column=6).value = ws2.cell(None, nsx_code_match_row_index, 2).value
                #print("----")
            nsx_code_match_row_index = nsx_code_match_row_index+1
        # reset the counter for next loop    
    nsx_code_match_row_index = 1

print(component_code_list)
new_bom_wb.save(filename = excel_path_suffix+'sample_book2.xlsx')
print("Finish excel mapping automation tool")