import os
import fitz

def style_extractor(pdf_dir: str, pdf_name: str) -> list[dict]:
    document = fitz.open(os.path.join(pdf_dir,pdf_name))
    styled_text = []

    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        blocks = page.get_text('dict')['blocks']

        for block in blocks:
            if 'lines' in block:
                for line in block['lines']:
                    for span in line['spans']:
                        text = span['text']
                        font = span['font']
                        font_size = span['size']
                        bold = "bold" in font.lower()

                        styled_text.append({
                            "text": text,
                            "font": font,
                            "font_size": font_size,
                            "bold": bold,
                        })

    return styled_text


DIRECTORY = '2022BC/'
NAME = '0_2022BC_Chapter01_AdministrationWBwm.pdf'

text_data = style_extractor(DIRECTORY, NAME)

for item in text_data:
    print(f"Text: {item['text']}")
    print(f"Font: {item['font']}, Size: {item['font_size']}, Bold: {item['bold']}")
    print("-" * 40)
