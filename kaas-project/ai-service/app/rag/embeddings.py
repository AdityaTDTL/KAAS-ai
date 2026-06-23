from sentence_transformers import SentenceTransformer



model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



def create_embeddings(chunks):

    texts = []


    for chunk in chunks:

        texts.append(
            chunk["content"]
        )


    vectors = model.encode(
        texts
    )


    return vectors