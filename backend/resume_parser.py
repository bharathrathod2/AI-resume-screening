import io
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(path_or_file):
    reader = PdfReader(path_or_file)
    texts = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return "\n".join(texts)

def extract_text_from_docx(path_or_file):
    doc = Document(path_or_file)
    texts = [p.text for p in doc.paragraphs]
    return "\n".join(texts)

def extract_text(file_stream, filename):
    fname = filename.lower()
    if fname.endswith('.pdf'):
        return extract_text_from_pdf(file_stream)
    elif fname.endswith('.docx') or fname.endswith('.doc'):
        return extract_text_from_docx(file_stream)
    else:
        return file_stream.read().decode('utf-8', errors='ignore')