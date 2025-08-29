from openpyxl import load_workbook
from openpyxl.workbook.defined_name import DefinedName

wb = load_workbook('Смета3.xlsx')



new_dname = DefinedName(name="Print_Title", attr_text="")
wb.defined_names.add(new_dname)
del wb.defined_names['Print_Title']


wb.save("Смета3.xlsx")