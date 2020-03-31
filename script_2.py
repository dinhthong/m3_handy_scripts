from openpyxl import Workbook
import openpyxl
print("Hello world")
file = "file_goc/EBOM_VEE-B01_Lan 11_Kien.xlsx"
wb = openpyxl.load_workbook(file, read_only=True)
#print(wb.sheetnames)
# Select a specific sheet to work
ws = wb["PL6_BOM_machchinh"]
ma_nsx_list = []
# iterate every row in column 
i = 1
for row in ws.iter_rows("I"):
    for cell in row:
        # limit to the rows where Ma NSX are available
        # note that some cases we must manually link in order to complete an Excel sheet. 
        if i>=14 and i<=147:
           # print([i,cell.value])
            #print(i)
            #print(cell.value)
            # Index value
            ma_nsx_list.append([i,cell.value])
            #if cell.value == "01111252":
             #   print("Hello world 2") #change column number for any cell value you want
                # print index
        # increase row index
        i = i+1
# print the list contain all ma nxs to map to target file along with its row index in previous file to Danh muc vat tu LINH KIEN.xlsx
print(ma_nsx_list)
file1 = "file_goc/Danh muc vat tu LINH KIEN.xlsx"
wb1 = openpyxl.load_workbook(file1, read_only=True)
print(wb1.sheetnames) 
