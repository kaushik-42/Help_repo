import openpyxl
from openpyxl.styles import PatternFill

# Load the workbook and select the sheet
workbook_path = 'your_excel_file.xlsx'
column_letter = 'A'  # Change this to the letter of the column you are interested in

wb = openpyxl.load_workbook(workbook_path)
sheet = wb.active

# Define the RGB color code for yellow
yellow_rgb = 'FFFF00'

highlighted_rows = []

# Iterate through the rows in the specified column
for row in range(1, sheet.max_row + 1):
    cell = sheet[f"{column_letter}{row}"]
    if cell.fill and cell.fill.fgColor and cell.fill.fgColor.rgb == yellow_rgb:
        highlighted_rows.append(row)

# Print or process the highlighted rows
print("Rows with yellow highlights in column", column_letter, ":", highlighted_rows)
