# Building Code RAG

## PDF Data Processing for RAG (Retrieval-Augmented Generation)

This project extracts and processes text from a collection of PDFs to build a foundation for a Retrieval-Augmented Generation (RAG) model. The goal is to efficiently extract text, chunk it logically, generate embeddings, and store them in a vector database for fast retrieval and integration with a language model.

## Project Overview

This project focuses on extracting structured text data from a set of PDF documents using `PyMuPDF` (`fitz`). The extracted text is processed into blocks based on the document's layout, which are then embedded using a pre-trained model. These embeddings are stored in a vector database for efficient similarity-based retrieval.

## Data Processing Workflow

1. **Extract Text Blocks from PDFs**: Extract text content in logical blocks using PyMuPDF. This method leverages the document's layout to group text into coherent chunks.
2. **Generate Embeddings**: Use a pre-trained model (`all-MiniLM-L6-v2` or similar) to generate embeddings for each text block.
3. **Store Embeddings in a Vector Database**: Store the generated embeddings in a vector database (such as FAISS) for efficient retrieval.
4. **Query the Vector Database**: Retrieve relevant text blocks based on a user-provided query.

### Requirements

- Python 3.8+
- PyMuPDF (`fitz`)
- sentence-transformers
- faiss-cpu (or faiss-gpu for GPU support)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/marcoscandroglio/building-code-rag.git
   cd building-code-rag
