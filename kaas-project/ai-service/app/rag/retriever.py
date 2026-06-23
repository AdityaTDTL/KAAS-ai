import faiss
import pickle
from embeddings import model



def load_vector_store():


    index = faiss.read_index(

        "data/vector_db/index.faiss"

    )


    with open(

        "data/vector_db/chunks.pkl",
        "rb"

    ) as f:


        chunks = pickle.load(f)



    return index, chunks





def search_similar_chunks(
        question,
        top_k=1
):


    index, chunks = load_vector_store()



    question_vector = model.encode(
        [question]
    )



    distances, indexes = index.search(

        question_vector,

        top_k

    )



    results = []



    for i in indexes[0]:

        results.append(
            chunks[i]
        )


    return results