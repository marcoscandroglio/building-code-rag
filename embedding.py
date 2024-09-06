from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(blocks: list):
    embeddings = model.encode(blocks, convert_to_tensor=True)
    return embeddings
