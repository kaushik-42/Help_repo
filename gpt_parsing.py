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

(gpt_env) a847848@MACH9XRKY9W9F Experimentation % pip install --upgrade pip
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/pip/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/pip/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/pip/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/pip/
^[[A^[[A^[[A^[[AWARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/pip/
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))) - skipping
Requirement already up-to-date: pip in ./gpt_env/lib/python3.8/site-packages (19.2.3)
WARNING: You are using pip version 19.2.3, however version 24.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(gpt_env) a847848@MACH9XRKY9W9F Experimentation % pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --up
grade pip
Collecting pip
  ERROR: HTTP error 403 while getting https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl#sha256=ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc (from https://pypi.org/simple/pip/) (requires-python:>=3.7)
  ERROR: Could not install requirement pip from https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl#sha256=ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc because of error 403 Client Error: Forbidden for url: https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl
ERROR: Could not install requirement pip from https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl#sha256=ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc because of HTTP error 403 Client Error: Forbidden for url: https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl for URL https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl#sha256=ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc (from https://pypi.org/simple/pip/) (requires-python:>=3.7)
WARNING: You are using pip version 19.2.3, however version 24.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(gpt_env) a847848@MACH9XRKY9W9F Experimentation % 

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
