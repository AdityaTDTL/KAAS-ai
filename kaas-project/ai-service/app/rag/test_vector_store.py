from loader import load_documents
from splitter import split_documents
from embeddings import create_embeddings
from vector_store import create_vector_store

docs = load_documents(
    "../../data/documents"
)

chunks = split_documents(
    docs
)

vectors = create_embeddings(
    chunks
)

create_vector_store(
    vectors,
    chunks
)

print("Vector database created")
