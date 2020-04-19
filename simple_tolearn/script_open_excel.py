from openpyxl import Workbook
import openpyxl
print("Hello world")
file = "List of Items 31-03-2020.xlsx"
wb = openpyxl.load_workbook(file, read_only=True)
ws = wb.active
# iterate every row in column F
i = 1
for row in ws.iter_rows("F"):
    for cell in row:
        print(i)
        print(cell.value)
        # Index value
        i = i+1
        if cell.value == "01111252":
            print("Hello world 2") #change column number for any cell value you want
            # print index