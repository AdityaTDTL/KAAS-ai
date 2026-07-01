import os


def load_documents(folder_path):

    documents = []


    for file_name in os.listdir(folder_path):

        file_path = os.path.join(
            folder_path,
            file_name
        )


        if file_name.endswith(".txt"):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()


                documents.append({

                    "content": text,

                    "source": file_name

                })


    return documents