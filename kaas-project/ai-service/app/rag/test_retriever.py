from retriever import search_similar_chunks



question = "How does supervised learning work?"



results = search_similar_chunks(
    question
)



print("\nQUESTION:")
print(question)



print("\nRETRIEVED KNOWLEDGE:")



for result in results:

    print("----------------")

    print(result["content"])