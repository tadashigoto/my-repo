import fitz  # PyMuPDF
from PIL import Image
import os
import sys

def pdf_to_jpeg(pdf_path):
    # PDFファイルの存在を確認
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return

    # 入力PDFのディレクトリとファイル名を取得
    folder_path = os.path.dirname(pdf_path)
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # PDFを開く
    pdf_document = fitz.open(pdf_path)

    # 各ページをJPEGとして保存
    for page_number in range(len(pdf_document)):
        # ページをPixmap形式で取得
        page = pdf_document[page_number]
        pix = page.get_pixmap()

        # 出力ファイル名を決定
        output_file = os.path.join(folder_path, f"{file_name}_page_{page_number + 1}.jpeg")

        # JPEGとして保存
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        image.save(output_file, "JPEG")
        print(f"Saved: {output_file}")

    pdf_document.close()

if __name__ == "__main__":
    # コマンドライン引数からPDFファイルパスを取得
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_jpeg_converter.py <pdf_file_path>")
    else:
        pdf_path = sys.argv[1]
        pdf_to_jpeg(pdf_path)
