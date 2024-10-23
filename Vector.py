from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example document and keywords from cover page
document_text = """
Python is widely used in various applications like web development, machine learning, and more. 
Data science, in particular, has seen great advancements thanks to Python libraries like NumPy and Pandas.
"""

cover_page_keywords = ["Python", "machine learning", "data science", "NumPy"]

# Generate embeddings for the keywords and the document
keyword_embeddings = model.encode(cover_page_keywords)
document_embedding = model.encode([document_text])

# Compute cosine similarities
similarities = cosine_similarity(keyword_embeddings, document_embedding)

# Set a threshold for determining if a keyword is present
threshold = 0.5

# Check if each keyword is present in the document
for i, keyword in enumerate(cover_page_keywords):
    if similarities[i][0] > threshold:
        print(f'Keyword "{keyword}" found in the document with similarity: {similarities[i][0]:.2f}')
    else:
        print(f'Keyword "{keyword}" not found in the document')
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a pre-trained transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the keywords for each category
categories = {
    "Category 1": ["keyword1", "keyword2", "keyword3"],
    "Category 2": ["keyword4", "keyword5", "keyword6"],
    "Category 3": ["keyword7", "keyword8", "keyword9"],
    "Category 4": ["keyword10", "keyword11", "keyword12"],
    # Add more categories as needed
    "Category 5": ["keyword13", "keyword14", "keyword15"],
    "Category 6": ["keyword16", "keyword17", "keyword18"],
    "Category 7": ["keyword19", "keyword20", "keyword21"],
    "Category 8": ["keyword22", "keyword23", "keyword24"]
}

# Example new document
new_document_text = """
Python is widely used in various applications like web development, machine learning, and more. 
Data science, in particular, has seen great advancements thanks to Python libraries like NumPy and Pandas.
"""

# Embed the new document
new_document_embedding = model.encode([new_document_text])

# Dictionary to store category scores
category_scores = {}

# Loop over each category and calculate the similarity with the new document
for category, keywords in categories.items():
    # Embed the keywords for the current category
    keyword_embeddings = model.encode(keywords)
    
    # Calculate cosine similarity between document and category keywords
    similarity = cosine_similarity(keyword_embeddings, new_document_embedding)
    
    # Calculate the average similarity for the current category
    avg_similarity = np.mean(similarity)
    
    # Store the score in the dictionary
    category_scores[category] = avg_similarity

# Find the category with the highest similarity score
best_category = max(category_scores, key=category_scores.get)
best_score = category_scores[best_category]

# Output the category classification
print(f'The new document belongs to: {best_category} with a similarity score of {best_score:.2f}')

# Optionally, print all scores for each category
for category, score in category_scores.items():
    print(f'Category: {category}, Similarity Score: {score:.2f}')

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a pre-trained transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example: 'new_document_text' in the form of a list of strings (OCR data)
new_document_text = [
    "1/26/23, 6:54 AM", 
    "From: JLT CONSULTING", 
    "Patient Name:", 
    "Rheumatology Enrollment Form", 
    "Medications", 
    "Allergies", 
    "Height", 
    "Weight"
]

# Define the keywords for each category (example categories)
categories = {
    "Healthcare": ["Patient", "Enrollment", "Medications", "Height", "Weight", "Allergies", "Consulting"],
    "Finance": ["Invoice", "Payment", "Due Date", "Amount", "Account", "Balance", "Transaction"],
    "Technology": ["Server", "Cloud", "Deployment", "API", "Database", "Software", "Architecture"],
    # Add more categories and their relevant keywords
}

# Function to calculate document similarity to each category
def classify_document(new_document_text, categories):
    # Convert the document (list of strings) to a single embedding for each chunk
    document_embeddings = model.encode(new_document_text)
    
    # Dictionary to store category scores
    category_scores = {}

    # Loop over each category and calculate the similarity with the new document
    for category, keywords in categories.items():
        # Embed the keywords for the current category
        keyword_embeddings = model.encode(keywords)
        
        # Calculate cosine similarity between document embeddings and category keywords
        similarity_scores = cosine_similarity(keyword_embeddings, document_embeddings)
        
        # Calculate the average similarity for the current category
        avg_similarity = np.mean(similarity_scores)
        
        # Store the score in the dictionary
        category_scores[category] = avg_similarity

    # Find the category with the highest similarity score
    best_category = max(category_scores, key=category_scores.get)
    best_score = category_scores[best_category]

    return best_category, best_score, category_scores

# Perform classification
best_category, best_score, all_scores = classify_document(new_document_text, categories)

# Output the classification results
print(f'The document belongs to: {best_category} with a similarity score of {best_score:.2f}')

# Optionally, print scores for all categories
for category, score in all_scores.items():
    print(f'Category: {category}, Similarity Score: {score:.2f}')
