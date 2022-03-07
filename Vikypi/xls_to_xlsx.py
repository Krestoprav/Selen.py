import win32com.client as win32
import os

file = open(rf'C:\Users\User\Desktop\Python\Vikypi\papka.txt', 'r', encoding='utf-8')
papka=file.readline()
file.close()

print(papka)
files=os.listdir(papka)
print(files)

for file in files:

    fname = rf'{papka}\{file}'
    print(fname)
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat=51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()

