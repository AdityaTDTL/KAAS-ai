import faiss
import pickle
import os

def create_vector_store(
        vectors,
        chunks
):
    dimension = len(
        vectors[0]
    )

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(vectors)

    os.makedirs(
        "data/vector_db",
        exist_ok=True
    )

    faiss.write_index(
        index,
        "data/vector_db/index.faiss"
    )

    with open(
        "data/vector_db/chunks.pkl",
        "wb"
    ) as f:
        pickle.dump(
            chunks,
            f
        )

    return index