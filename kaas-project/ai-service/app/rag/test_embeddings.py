from loader import load_documents
from splitter import split_documents
from embeddings import create_embeddings

docs = load_documents(
    "../../data/documents"
)

chunks = split_documents(
    docs
)

vectors = create_embeddings(
    chunks
)

print(vectors)

print(
    len(vectors)
)
