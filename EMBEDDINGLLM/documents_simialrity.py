from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


embedding = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=256)

documents = [
    "India is a large and diverse country in South Asia.",
     "It is known for its rich culture, history, and traditions.",
     "India is the world's largest democracy and has a population of over one billion people.",
     "The country is famous for landmarks like Taj Mahal and for its many languages and festivals.",
     "India is also growing rapidly in science, technology, education, and industry."
]


query = "Which country known as rich culture"

doc_embedd=embedding.embed_documents(documents)

query_embedd= embedding.embed_query(query)


print(cosine_similarity([query_embedd],doc_embedd))