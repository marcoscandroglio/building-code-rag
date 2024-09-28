import os
import json
from extract_text import extract_text, merge_blocks
from embedding import generate_embeddings
from vector_db import create_vector_index

DIRECTORY = '2022BC/'
os.makedirs('data', exist_ok=True)

text_blocks = extract_text(DIRECTORY)
merged_text = merge_blocks(text_blocks)

with open('data/pdf_blocks.json', 'w') as file:
    json.dump(merged_text, file)

embeddings = generate_embeddings(merged_text)
create_vector_index(embeddings)
