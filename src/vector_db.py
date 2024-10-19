import torch
import faiss
from sentence_transformers import SentenceTransformer


def create_vector_index(
    embeddings: torch.Tensor,
    index_path: str = 'saved_data/vector_index.faiss'
) -> faiss.IndexFlatL2:
    """
    Creates and saves a FAISS vector index using the provided embeddings.

    Args:
        embeddings (torch.Tensor): A PyTorch tensor containing the embeddings to index. 
                                   The shape should be (num_samples, dimension).
        index_path (str, optional): The path where the vector index will be saved. 
                                    Defaults to 'saved_data/vector_index.faiss'.

    Returns:
        faiss.IndexFlatL2: The created FAISS index.
    """

    embeddings_np = embeddings.cpu().detach().numpy()
    dimension = embeddings_np.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_np)
    faiss.write_index(index, index_path)
    return index


def load_vector_index(
    index_path: str = 'saved_data/vector_index.faiss'
) -> faiss.IndexFlatL2:
    """
    Loads a FAISS vector index from the specified path.

    Args:
        index_path (str, optional): The path where the vector index is saved. 
                                    Defaults to 'saved_data/vector_index.faiss'.

    Returns:
        faiss.IndexFlatL2: The loaded FAISS index.
    """

    return faiss.read_index(index_path)


def search_vector_db(
    query: str, 
    model: SentenceTransformer, 
    index: faiss.IndexFlatL2, 
    pdf_blocks: list[str], 
    top_k: int = 5
) -> list[str]:
    """
    Searches the vector database for the closest matches to a given query.

    Args:
        query (str): The query string to encode and search for.
        model (SentenceTransformer): A model used to encode the query string into an embedding.
        index (faiss.IndexFlatL2): The FAISS index to search in.
        pdf_blocks (list): A list of text blocks to retrieve from.
        top_k (int, optional): The number of top matches to return. Defaults to 5.

    Returns:
        list: A list of the top-k matched text blocks from the pdf_blocks.
    """

    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    distances, indices = index.search(query_embedding, top_k)
    return [pdf_blocks[i] for i in indices[0]]
