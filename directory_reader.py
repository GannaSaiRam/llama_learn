import os

import dotenv

from llama_index.legacy import VectorStoreIndex
from llama_index.legacy.readers import SimpleDirectoryReader

dotenv.load_dotenv()


def main(directory: str) -> None:
    directory_docs = SimpleDirectoryReader(directory).load_data()
    vec_index = VectorStoreIndex.from_documents(directory_docs)
    query_engine = vec_index.as_query_engine()
    response = query_engine.query("Where is the name of this person? Where does he study?")
    print(response)
    response = query_engine.query("Give me his few work experience details")
    print(response)


if __name__ == "__main__":
    main(directory=os.path.join(os.getcwd(), 'test_directory'))
