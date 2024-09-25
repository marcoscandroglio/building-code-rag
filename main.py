import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from vector_db import load_vector_index, search_vector_db

def load_data(data_dir='data/'):
    json_file_name = [name for name in os.listdir(data_dir) if '.json' in name]
    json_file_path = os.path.join(data_dir, json_file_name[0])

    with open(json_file_path, 'r') as file:
        pdf_blocks = json.load(file)

    return pdf_blocks

blocks = load_data()
print(len(blocks))
print(type(blocks))

if __name__ == '__main__':
    FAISS_DIRECTORY = 'data/vector_index.faiss'

    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector_index = load_vector_index(FAISS_DIRECTORY)
    blocks = load_data()

    while True:
        user_query = input('What is your code question? (type q to quit):\n')
        if user_query == 'q':
            break

        top_k_results = search_vector_db(user_query, model, vector_index, blocks, )

        print('\n')
        for result in top_k_results:
            print(result)
            print('\n')
        print('-' * 100)
        print('\n')
