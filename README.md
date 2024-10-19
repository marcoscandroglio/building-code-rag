# Building Code RAG

## PDF Data Processing for RAG (Retrieval-Augmented Generation)

This project extracts and processes text from a collection of PDFs to build a foundation for a **Retrieval-Augmented Generation (RAG)** model. The goal is to efficiently extract text, chunk it logically, generate embeddings, and store them in a vector database for fast retrieval and integration with a language model.

## Project Overview

The project focuses on extracting structured text data from a set of PDF documents using `PyMuPDF` (`fitz`). The extracted text is processed into blocks based on the document's layout, which are then embedded using a pre-trained model. These embeddings are stored in a vector database for efficient similarity-based retrieval.

A **Command Line Interface (CLI)** allows users to ask questions about the content of the PDFs. The relevant sections from the documents are retrieved based on user queries and presented as output.

## Data Processing Workflow

1. **Extract Text Blocks from PDFs**: Extract text content in logical blocks using PyMuPDF. This method leverages the document's layout to group text into coherent chunks.
2. **Filter and Merge Blocks**: Filter out short blocks and merge section headings with adjacent content to provide context-rich chunks.
3. **Generate Embeddings**: Use a pre-trained model (`all-MiniLM-L6-v2` or similar) to generate embeddings for each text block.
4. **Store Embeddings in a Vector Database**: Store the generated embeddings in a vector database (such as FAISS) for efficient retrieval.
5. **Query the Vector Database**: Retrieve relevant text blocks based on a user-provided query using the CLI.

## Usage Instructions

1. **Collect PDFs to Process**: Run the webscraping script provided to retrieve the building code text by running:

      `python -m src.get_pdfs`

2. **Preprocess the PDFs and Create the Vector Database**: Extract text blocks, generate embeddings, and create a vector index from your PDF collection. The preprocessed data and vector index are saved for efficient querying.

      `python -m src.preprocess_data`

3. **Run the CLI**: Use the command line interface to ask questions about the content of the PDFs. The CLI retrieves and displays relevant sections based on the similarity of the query to the stored embeddings.

      `python -m src.main`

## Example Queries

Here is a sample query and corresponding response from the CLI:

### Query 1:  
```plaintext
Please enter your question about building codes or regulations (type 'q' to quit):
What dimensions are critical for stairs?

Relevant Sections:
------------------

3303.11.2 Stairs during building construction or enlargements. During new building construction or the en-
largement of an existing building, stairs shall be provided at all locations where a permanent stair will be required 
and shall serve all floors. At least one of the provided stairs must be of permanent construction for its full length; 
in all other locations, the stairs may be of temporary or permanent construction.


1011.5.4 Dimensional uniformity. Stair treads and risers shall be of uniform size and shape. The tolerance between 
the largest and smallest riser height or between the largest and smallest tread depth shall not exceed 3/8 inch (9.5 
mm) in any flight of stairs. The greatest winder tread depth at the walkline within any flight of stairs shall not 
exceed the smallest by more than 3/8 inch (9.5 mm).


3. During the construction or enlargement of a building whose primary structural system consists of struc-
tural steel, where it is not feasible to provide one or more permanent stairs to serve all floors that are at 
least 4 stories or 40 feet (12 192 mm) below the topmost working deck, whichever is less, all stairs shall 
be of their permanent construction up to the level of the topmost completed steel floor, and temporary 
stairs, acceptable to the commissioner, shall be brought up in all locations to serve all remaining floors 
that are at least 4 stories or 40 feet (12 192 mm) below the topmost working deck, whichever is less. At a 
minimum, the temporary stairs shall be made of non-combustible material, be equipped with adequate 
handrails, be provided with landings that are level with the adjoining floor, and have riser height and tread 
depths that are uniform, within 1/4 inch (6 mm), for each flight of stairs.


3.3. Tolerances. The greatest riser height, tread depth, and nosing projection, within any flight of stairs 
shall not exceed the smallest by more than 3/4 inch (9.5 mm).


MEANS OF EGRESS apart equal to not less than one-half of the length of the maximum overall diagonal dimension of the building or 
area to be served measured in a straight line between them. Stairs sharing any common wall, floor, ceiling, scissor 
stair assembly, or other enclosure shall be counted as one exit stairway.


----------------------------------------------------------------------------------------------------
```

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
   python -m src.get_pdfs
   python -m src.preprocess_data
   python -m src.main
