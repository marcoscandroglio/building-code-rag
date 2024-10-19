import os
import json
from src.extract_text import extract_text, merge_blocks
from src.embedding import generate_embeddings
from src.vector_db import create_vector_index

PDF_DIRECTORY = 'saved_data/2022BC/'
os.makedirs('data', exist_ok=True)

text_blocks = extract_text(PDF_DIRECTORY)
merged_text = merge_blocks(text_blocks)

with open('saved_data/pdf_blocks.json', 'w', encoding='utf-8') as file:
    json.dump(merged_text, file)

embeddings = generate_embeddings(merged_text)
create_vector_index(embeddings)
