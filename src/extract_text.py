import os
import fitz


def extract_text(pdf_dir: str) -> list:
    """
    Extracts text blocks from all PDF files in a specified directory.

    This function processes each PDF file in the provided directory and extracts
    text blocks based on the existing structure of each PDF page. The extracted
    blocks are appended to a list, which is returned.

    Args:
        pdf_dir (str): The directory containing the PDF files to be processed.

    Returns:
        list: A list of extracted text blocks from all the PDF files in the directory.
    """

    block_list = []
    for file in os.listdir(pdf_dir):
        file_path = os.path.join(pdf_dir, file)
        # print(file_path)
        document = fitz.open(file_path)

        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            blocks = page.get_text('blocks')

            for block in blocks:
                block_text = block[4].strip()
                if block_text:
                    block_list.append(block_text)

    return block_list


def merge_blocks(text_blocks: list, min_block_len: int=5) -> list:
    """
    Merges smaller text blocks with subsequent blocks to create context-rich responses.

    This function concatenates smaller text blocks with the following block to ensure
    that short, fragmented pieces of text are merged into more coherent and contextually
    rich blocks. The minimum word count threshold for determining a "small block" can be specified.

    Args:
        text_blocks (list): A list of text blocks to be merged.
        min_block_len (int, optional): The minimum number of words in a block to be considered
                                       contextually complete. Defaults to 5.

    Returns:
        list: A list of merged text blocks that are more contextually coherent.
    """

    merged_blocks = []
    curr_block = ''

    for block in text_blocks:

        if len(block.split()) < min_block_len:
            curr_block += ' ' + block

        elif len(block.split()) >= min_block_len and curr_block:
            curr_block += ' ' + block
            merged_blocks.append(curr_block.strip())
            curr_block = ''

        else:
            merged_blocks.append(block)

    if curr_block:
        merged_blocks.append(curr_block.strip())

    return merged_blocks


if __name__ == '__main__':
    DIRECTORY = '../saved_data/2022BC/'
    # pdf_blocks = extract_text(DIRECTORY)
    files = os.listdir(DIRECTORY)
    for f in files:
        print(f)

    # for i, text_block in enumerate(pdf_blocks):
    #     print(f"Block {i + 1}:\n{text_block}\n")
    #     print("-" * 100)
