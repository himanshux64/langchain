from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()
documents = [
    "Bihar is the Diverse state ",
    " Delhi is the Capital of India ",
    "Machine learning is the subfield of Ai"
]

embedded = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)

result=embedded.embed_documents(documents)

print(str(result))