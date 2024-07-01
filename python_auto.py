import openpyxl
from openpyxl.styles import PatternFill

# Load the workbook and select the sheet
workbook_path = 'your_excel_file.xlsx'
column_letter = 'A'  # Change this to the letter of the column you are interested in

wb = openpyxl.load_workbook(workbook_path)
sheet = wb.active

# Define the RGB color code for yellow
yellow_rgb = 'FFFF00'

# Find the column letter based on the column name in the header row
column_letter = None
for cell in sheet[1]:  # Assuming the first row contains the column headers
    if cell.value == column_name:
        column_letter = cell.column_letter
        break

if not column_letter:
    raise ValueError(f"Column '{column_name}' not found in the header row.")

highlighted_rows = []

# Iterate through the rows in the specified column
for row in range(1, sheet.max_row + 1):
    cell = sheet[f"{column_letter}{row}"]
    fill = cell.fill
    if fill and fill.start_color:
        fg_color = fill.start_color
        if fg_color.type == 'rgb' and fg_color.rgb == yellow_rgb:
            highlighted_rows.append(row)
        elif fg_color.type == 'indexed' and fg_color.index == 5:  # Yellow index
            highlighted_rows.append(row)

# Print or process the highlighted rows
print("Rows with yellow highlights in column", column_letter, ":", highlighted_rows)
