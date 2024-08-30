import fitz


def extract_text(pdf_path: str) -> list:
    '''
    Function to divide the source PDF into text blocks
    according to its existing structure
    '''

    document = fitz.open(pdf_path)
    block_list = []

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        blocks = page.get_text('blocks')

        for block in blocks:
            block_text = block[4].strip()
            if block_text:
                block_list.append(block_text)

    return block_list


if __name__ == '__main__':
    DIRECTORY = '2022BC/0_2022BC_Chapter01_AdministrationWBwm.pdf'
    pdf_blocks = extract_text(DIRECTORY)

    for i, text_block in enumerate(pdf_blocks):
        print(f"Block {i + 1}:\n{text_block}\n")
        print("-" * 100)
