from langchain_text_splitters import RecursiveCharacterTextSplitter



def split_documents(documents):


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=200,

        chunk_overlap=30   

    )


    chunks = []


    for doc in documents:


        split_texts = splitter.split_text(
            doc["content"]
        )


        for text in split_texts:

            chunks.append({

                "content": text,

                "source": doc["source"]

            })


    return chunks