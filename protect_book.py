#ブックを保護する

from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

wb = load_workbook("見積書.xlsx")

wb.security = WorkbookProtection(workbookPassword='test', lockStructure=True)

wb.save("見積書_ブック保護.xlsx")