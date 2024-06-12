(gpt_env) a847848@MACH9XRKY9W9F Experimentation % pip install openai pytesseract pdf2image
Collecting openai
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/openai/
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/openai/
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/openai/
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/openai/
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/openai/
  Could not fetch URL https://pypi.org/simple/openai/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/openai/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))) - skipping
  ERROR: Could not find a version that satisfies the requirement openai (from versions: none)
ERROR: No matching distribution found for openai
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))) - skipping
(gpt_env) a847848@MACH9XRKY9W9F Experimentation % 

ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE. If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them.
    pip from https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl#sha256=ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc:
        Expected sha256 ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc
             Got        19f68cf0bd1335e7904632ec0d2220b04b428efb3ff413e5753bdaf0edbbabd6

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

(.venv) a847848@MACH9XRKY9W9F Experimemts_AIHUB % python3 hello_world.py                
Traceback (most recent call last):
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pytesseract/pytesseract.py", line 255, in run_tesseract
    proc = subprocess.Popen(cmd_args, **subprocess_args())
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/subprocess.py", line 1821, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tesseract'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 61, in <module>
    result = main(API_KEY, PDF_PATH)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 49, in main
    document_content = extract_text_from_pdf(pdf_path)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 16, in extract_text_from_pdf
    text += pytesseract.image_to_string(img)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pytesseract/pytesseract.py", line 423, in image_to_string
    return {
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pytesseract/pytesseract.py", line 426, in <lambda>
    Output.STRING: lambda: run_and_get_output(*args),
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pytesseract/pytesseract.py", line 288, in run_and_get_output
    run_tesseract(**kwargs)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pytesseract/pytesseract.py", line 260, in run_tesseract
    raise TesseractNotFoundError()
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.




During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 56, in <module>
    result = main(API_KEY, PDF_PATH)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 44, in main
    document_content = extract_text_from_pdf(pdf_path)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/hello_world.py", line 8, in extract_text_from_pdf
    pages = convert_from_path(pdf_path)
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pdf2image/pdf2image.py", line 127, in convert_from_path
    page_count = pdfinfo_from_path(
  File "/Users/a847848/Desktop/Experimemts_AIHUB/.venv/lib/python3.9/site-packages/pdf2image/pdf2image.py", line 607, in pdfinfo_from_path
    raise PDFInfoNotInstalledError(
pdf2image.exceptions.PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?

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
