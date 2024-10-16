# pip install sentence-transformers faiss-cpu

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

def build_cover_page_index(cover_texts, model_name='all-MiniLM-L6-v2'):
    """
    Builds a vector index for cover pages.

    Args:
        cover_texts (list): List of cover page texts.
        model_name (str): The name of the embedding model.

    Returns:
        index: FAISS index of cover page embeddings.
        model: Embedding model used.
        cover_embeddings: Numpy array of cover page embeddings.
    """
    model = SentenceTransformer(model_name)
    cover_embeddings = model.encode(cover_texts, convert_to_numpy=True)
    dimension = cover_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(cover_embeddings)
    return index, model, cover_embeddings

def is_cover_page_vector(ocr_text, index, model, threshold=0.75):
    """
    Determines if a page is a cover page using vector similarity.

    Args:
        ocr_text (str): OCR text of the page.
        index: FAISS index of cover page embeddings.
        model: Embedding model.
        threshold (float): Similarity threshold.

    Returns:
        bool: True if page is a cover page, False otherwise.
    """
    embedding = model.encode([ocr_text], convert_to_numpy=True)
    D, _ = index.search(embedding, k=1)
    similarity = 1 - D[0][0] / 2  # Cosine similarity approximation
    return similarity >= threshold

# Example usage

# Sample cover page texts (could be actual cover pages)
cover_texts = [
    """PROJECT REPORT

    ON

    MARKET ANALYSIS OF THE RETAIL INDUSTRY

    Submitted by:

    John Doe

    Supervisor:

    Dr. Jane Smith

    Department of Business Administration

    University of Example

    CONFIDENTIAL
    """,
    """ANNUAL FINANCIAL STATEMENTS

    Company XYZ

    For the Year Ended December 31, 2022

    Prepared by:

    Finance Department

    Confidential Document
    """
]

# Build the cover page index
index, model, cover_embeddings = build_cover_page_index(cover_texts)

# OCR text pages
ocr_text_pages = [
    """PROJECT REPORT

    ON

    MARKET ANALYSIS OF THE RETAIL INDUSTRY

    Submitted by:

    John Doe

    Supervisor:

    Dr. Jane Smith

    Department of Business Administration

    University of Example

    CONFIDENTIAL
    """,
    """1. Introduction

    The retail industry has undergone significant changes over the past decade...
    """
]

pages_to_send = []
for page_num, ocr_text in enumerate(ocr_text_pages):
    if not is_cover_page_vector(ocr_text, index, model):
        pages_to_send.append(ocr_text)
    else:
        print(f"Page {page_num + 1} identified as cover page and excluded.")

print("\nPages to send to ChatGPT:")
for idx, page in enumerate(pages_to_send):
    print(f"\n--- Page {idx + 1} ---\n{page}")
