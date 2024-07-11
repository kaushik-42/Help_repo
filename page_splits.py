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

# For all the files:
import os
from PyPDF2 import PdfReader, PdfWriter

# Paths to your files
pdf_folder_path = 'your_pdf_folder'  # Update this to your folder containing PDF files
output_folder = 'extracted_pages'  # Update this to your desired output folder

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all PDF files in the specified folder
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]

# Process each PDF file in the folder
for pdf_file_name in pdf_files:
    pdf_file_path = os.path.join(pdf_folder_path, pdf_file_name)
    file_name, _ = os.path.splitext(pdf_file_name)

    # Read the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)

        # Extract each page and save it as a separate PDF
        for page_no in range(1, len(reader.pages) + 1):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_no - 1])  # Page numbers are 0-indexed in PyPDF2

            # Define the output file path with the page number
            output_file_path = os.path.join(output_folder, f"{file_name}_{page_no}.pdf")

            # Check if the output file already exists
            if os.path.exists(output_file_path):
                print(f"Output file {output_file_path} already exists. Skipping.")
                continue

            # Save the extracted page to the output folder
            with open(output_file_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Extracted page {page_no} from {pdf_file_path} to {output_file_path}")

print("Extraction complete.")

            continue

        # Extract the specified page
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(page_no - 1))  # Page numbers are 0-indexed in PyPDF2

        # Save the extracted page to the output folder
        # Save the extracted page to the output folder
        output_file_path = os.path.join(output_folder, file_name + '.pdf')
        with open(output_file_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Extracted page {page_no} from {pdf_file_path} to {output_file_path}")

print("Extraction complete.")

