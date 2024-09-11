import faiss
import numpy as np

def create_vector_index(embeddings, index_path='vector_index.faiss'):
    embeddings_np = embeddings.cpu().detach().numpy()
    dimension = embeddings_np.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_np)
    faiss.write_index(index, index_path)
    return index


def load_vector_index(index_path='vector_index.faiss'):
    return faiss.read_index(index_path)


def search_vector_db(query, model, index, pdf_blocks, top_k=5):
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    distances, indices = index.search(query_embedding, top_k)
    return [pdf_blocks[i] for i in indices[0]]
