from sentence_transformers import SentenceTransformer, util

# Initialize model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define categories
categories = {
    'Category 1': ['apple', 'banana', 'strawberries'],
    'Category 2': ['carrot', 'potato', 'onion'],
    'Category 3': ['fish', 'chicken', 'beef'],
    'Category 4': ['monopoly', 'board games']
}

# Compute category embeddings
category_embeddings = {}
for category, items in categories.items():
    item_embeddings = model.encode(items)
    category_embedding = item_embeddings.mean(axis=0)
    category_embeddings[category] = category_embedding

# Compute text embedding
text = "I love board games and also love blueberries"
text_embedding = model.encode(text)

# Calculate similarities
similarities = {}
for category, embedding in category_embeddings.items():
    similarity = util.cos_sim(text_embedding, embedding).item()
    similarities[category] = similarity

# Sort categories by similarity
sorted_categories = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
print(sorted_categories)
