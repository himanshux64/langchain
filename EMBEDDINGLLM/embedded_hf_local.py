from langchain_huggingface import HuggingFaceEmbeddings

embedded=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Bihar is the Diverse state ",
    " Delhi is the Capital of India ",
    "Machine learning is the subfield of Ai"
]

vector=embedded.embed_documents(documents)

print(str(vector))