import PyPDF2
import re
import sys

def read_pdf_metadata_pypdf2(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        info = reader.metadata
        print("Metadata using PyPDF2:")
        for key, value in info.items():
            print(f"{key}: {value}")

def read_pdf_metadata_regex(pdf_path):
    with open(pdf_path, 'rb') as f:
        content = f.read()
        content_str = content.decode('latin1')  # PDF content is often in Latin-1 encoding
        metadata = re.findall(r'/(\w+)\s*\((.*?)\)', content_str)
        print("\nMetadata using Regex:")
        for key, value in metadata:
            print(f"{key}: {value}")

def main(pdf_path):
    read_pdf_metadata_pypdf2(pdf_path)
    read_pdf_metadata_regex(pdf_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_metadata.py <path_to_pdf>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    main(pdf_path)
