from extract_text import extract_text
from embedding import generate_embeddings
from vector_db import create_vector_index

DIRECTORY = '2022BC/'

text_blocks = extract_text(DIRECTORY)
embeddings = generate_embeddings(text_blocks)
create_vector_index(embeddings)
