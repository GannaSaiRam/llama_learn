from dotenv import load_dotenv
from llama_index.legacy.readers import SimpleWebPageReader
from llama_index.legacy import VectorStoreIndex

load_dotenv()


def main(url: str) -> None:
    document_reader = SimpleWebPageReader(html_to_text=True)
    document = document_reader.load_data(urls=[url])
    vector_index = VectorStoreIndex.from_documents(documents=document)
    query_engine = vector_index.as_query_engine()
    response = query_engine.query("Give me synopsys in less than 100 words")
    print(response)


if __name__ == "__main__":
    main(url="https://en.wikipedia.org/wiki/Kalki_2898_AD")
