import os
import json
from sentence_transformers import SentenceTransformer
from src.vector_db import load_vector_index, search_vector_db

def load_data(data_dir: str='saved_data/') -> list:
    """
    Loads text block data from a JSON file in the specified directory.

    This function searches for a JSON file in the provided directory, reads it, and 
    loads its contents as a list of text blocks. It assumes that there is only one 
    JSON file in the specified directory.

    Args:
        data_dir (str, optional): The directory where the JSON file is stored. 
                                  Defaults to 'saved_data/'.

    Returns:
        list: A list of text blocks loaded from the JSON file.
    """

    json_file_name = [name for name in os.listdir(data_dir) if '.json' in name]
    json_file_path = os.path.join(data_dir, json_file_name[0])

    with open(json_file_path, 'r', encoding='utf-8') as file:
        pdf_blocks = json.load(file)

    return pdf_blocks


if __name__ == '__main__':
    FAISS_DIRECTORY = 'saved_data/vector_index.faiss'

    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector_index = load_vector_index(FAISS_DIRECTORY)
    blocks = load_data()

    while True:
        user_query = input('Please enter your question about building codes or regulations (type \'q\' to quit):\n')
        if user_query == 'q':
            break

        top_k_results = search_vector_db(user_query, model, vector_index, blocks, )

        print('\nRelevant Sections:')
        print('------------------\n')
        for result in top_k_results:
            print(result)
            print('\n')
        print('-' * 100)
        print('\n')
