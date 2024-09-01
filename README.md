# Building Code RAG

## PDF Data Processing for RAG (Retrieval-Augmented Generation)

This project extracts and processes text from a collection of PDFs to build a foundation for a Retrieval-Augmented Generation (RAG) model. The goal is to efficiently extract text, chunk it logically, and prepare it for integration with a vector database and a language model.

## Project Overview

This project focuses on extracting structured text data from a set of PDF documents using `PyMuPDF` (`fitz`). The extracted text is processed into blocks based on the document's layout, which can then be stored and retrieved for further question-answering and generation tasks.

## Data Processing Workflow

1. **Extract Text Blocks from PDFs**: Extract text content in logical blocks using PyMuPDF. This method leverages the document's layout to group text into coherent chunks.
2. **Store the Extracted Blocks**: The extracted blocks can be further processed, indexed, or stored in a vector database for retrieval tasks.

### Requirements

- Python 3.8+
- PyMuPDF (`fitz`)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
