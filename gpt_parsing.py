import openai
import pytesseract
from pdf2image import convert_from_path
import json

# Function to extract text from PDF using OCR
def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

# Function to call the GPT API
def call_gpt_api(api_key, document_content):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a document parser. Extract relevant details and format them as JSON."},
            {"role": "user", "content": f"Parse the following document and provide structured JSON output: {document_content}"}
        ]
    )

    return response['choices'][0]['message']['content']

# Function to perform post-processing on the GPT output
def post_process_gpt_output(gpt_output):
    # Convert the GPT output to JSON
    try:
        parsed_data = json.loads(gpt_output)
        # Example post-processing: normalize keys, calculate totals, etc.
        if "items" in parsed_data:
            total_amount = sum(item["price"] * item["quantity"] for item in parsed_data["items"])
            parsed_data["total_amount"] = total_amount
        return parsed_data
    except json.JSONDecodeError:
        return {"error": "Failed to parse GPT output as JSON"}

# Main function to execute the workflow
def main(api_key, pdf_path):
    document_content = extract_text_from_pdf(pdf_path)
    gpt_output = call_gpt_api(api_key, document_content)
    processed_data = post_process_gpt_output(gpt_output)
    return processed_data

# Example usage
if __name__ == "__main__":
    API_KEY = "your_openai_api_key"  # Replace with your OpenAI API key
    PDF_PATH = "path_to_your_pdf.pdf"  # Replace with the path to your PDF document

    result = main(API_KEY, PDF_PATH)
    print(json.dumps(result, indent=2))
import openai
import pytesseract
from pdf2image import convert_from_path
import json

# Function to extract text from PDF using OCR
def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

# Function to call the GPT API
def call_gpt_api(api_key, document_content):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a document parser. Extract relevant details and format them as JSON."},
            {"role": "user", "content": f"Parse the following document and provide structured JSON output: {document_content}"}
        ]
    )

    return response['choices'][0]['message']['content']

# Function to perform post-processing on the GPT output
def post_process_gpt_output(gpt_output):
    # Convert the GPT output to JSON
    try:
        parsed_data = json.loads(gpt_output)
        # Example post-processing: normalize keys, calculate totals, etc.
        if "items" in parsed_data:
            total_amount = sum(item["price"] * item["quantity"] for item in parsed_data["items"])
            parsed_data["total_amount"] = total_amount
        return parsed_data
    except json.JSONDecodeError:
        return {"error": "Failed to parse GPT output as JSON"}

# Main function to execute the workflow
def main(api_key, pdf_path):
    document_content = extract_text_from_pdf(pdf_path)
    gpt_output = call_gpt_api(api_key, document_content)
    processed_data = post_process_gpt_output(gpt_output)
    return processed_data

# Example usage
if __name__ == "__main__":
    API_KEY = "your_openai_api_key"  # Replace with your OpenAI API key
    PDF_PATH = "path_to_your_pdf.pdf"  # Replace with the path to your PDF document

    result = main(API_KEY, PDF_PATH)
    print(json.dumps(result, indent=2))
