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
