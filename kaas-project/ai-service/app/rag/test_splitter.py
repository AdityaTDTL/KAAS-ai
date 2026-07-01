from loader import load_documents
from splitter import split_documents

documents = load_documents(
    "../../data/documents"
)

chunks = split_documents(
    documents
)

for chunk in chunks:
    print("----------------")
    print(chunk["content"])
