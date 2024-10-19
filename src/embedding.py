import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(blocks: list) -> torch.Tensor:
    """
    Generates embeddings for a list of text blocks using a pre-trained model.

    This function encodes each text block into an embedding vector using a pre-trained
    model, typically a transformer-based model such as a SentenceTransformer. The embeddings
    are returned as a tensor for further processing or indexing.

    Args:
        blocks (list): A list of text blocks to be encoded into embeddings.

    Returns:
        torch.Tensor: A tensor containing the embeddings for the provided text blocks.
    """

    embeddings = model.encode(blocks, convert_to_tensor=True)
    return embeddings
