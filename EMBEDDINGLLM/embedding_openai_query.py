from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedded = OpenAIEmbeddings(model='text-embedding-ada-002',dimensions=32)

result=embedded.embed_query("Delhi is the capital of india")

print(str(result))