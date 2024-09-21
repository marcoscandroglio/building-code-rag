import os
import json
from extract_text import extract_text
from embedding import generate_embeddings
from vector_db import create_vector_index

DIRECTORY = '2022BC/'
os.makedirs('data', exist_ok=True)

text_blocks = extract_text(DIRECTORY)

with open('data/pdf_blocks.json', 'w') as file:
    json.dump(text_blocks, file)

embeddings = generate_embeddings(text_blocks)
create_vector_index(embeddings)
