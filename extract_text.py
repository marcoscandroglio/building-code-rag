import fitz
import os


def extract_text(pdf_dir: str) -> list:
    '''
    Function to divide the source PDF into text blocks
    according to its existing structure
    '''

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
    DIRECTORY = '2022BC/'
    pdf_blocks = extract_text(DIRECTORY)

    # for i, text_block in enumerate(pdf_blocks):
    #     print(f"Block {i + 1}:\n{text_block}\n")
    #     print("-" * 100)
