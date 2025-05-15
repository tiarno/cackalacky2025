import fitz  # PyMuPDF
import osc
from datetime import datetime
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def convert_pdf_date(pdf_date):
    try:
        return datetime.strptime(pdf_date[2:16], "%Y%m%d%H%M%S").isoformat()
    except: 
        return "Unknown"
    
def extract_text_and_metadata_from_pdf(pdf_path, chunk_size=1000, chunk_overlap=100):
    """Extract text and metadata from PDF with error handling"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    try:
        with fitz.open(pdf_path) as pdf:
            # Extract document-level metadata
            meta = pdf.metadata
            title = meta.get('title', os.path.basename(pdf_path))
            author = meta.get('author', 'Unknown')
            creation_date = convert_pdf_date(meta.get('creationDate', 'Unknown'))
            
            # Convert TOC to readable string
            toc = pdf.get_toc()
            toc_str = "\n".join([f"{'  '*(level-1)}- {title}" for level, title, _, _ in toc])

            # Process pages
            documents = []
            for page_num, page in enumerate(pdf.pages(), start=1):
                text = page.get_text().strip()
                if not text:
                    continue

                documents.append(Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path,
                        "title": title,
                        "author": author,
                        "creation_date": creation_date,
                        "page": page_num,
                        "toc": toc_str
                    }
                ))

            return text_splitter.split_documents(documents)
            
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return []

def main():
    pdf_directory = "./pdfs"  # <-- put all your pdfs here
    persist_directory = "./embeddings" # <-- this subdir will contain the saved vector database.
    
    # Load embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}  # Remove if using GPU
    )

    # Process all PDFs
    all_chunks = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            full_path = os.path.join(pdf_directory, filename)
            print(f"Processing: {filename}")
            chunks = extract_text_and_metadata_from_pdf(full_path)
            all_chunks.extend(chunks)

    # Create and persist vector store
    if all_chunks:
        vector_store = Chroma.from_documents(
            documents=all_chunks,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        vector_store.persist()
        print(f"Successfully created vector store with {len(all_chunks)} chunks")
    else:
        print("No valid PDFs found to process")

if __name__ == "__main__":
    main()
