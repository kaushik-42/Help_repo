import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# Paths to your files
required_list_path = 'file_required_list.txt'  # Update this to your required list file path
output_folder = 'extracted_pages'  # Update this to your desired output folder

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Step 4: Read the required list
with open(required_list_path, 'r') as file:
    lines = file.readlines()

# Process each entry in the required list
for line in lines:
    file_name, page_no, folder_location = line.strip().split('|')
    page_no = int(page_no)  # Convert page number to integer

    # Only process if the file name matches the highlighted values (assuming this is available from the previous script)
    if file_name not in matching_values:
        continue

    # Construct the full path to the PDF file
    pdf_file_path = os.path.join(folder_location, file_name + '.pdf')

    # Read the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = PdfFileReader(pdf_file)
        
        # Ensure the page number is valid
        if page_no < 1 or page_no > reader.numPages:
            print(f"Invalid page number {page_no} for file {pdf_file_path}. Skipping.")
            continue

        # Extract the specified page
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(page_no - 1))  # Page numbers are 0-indexed in PyPDF2

        # Save the extracted page to the output folder
