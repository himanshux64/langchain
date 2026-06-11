from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenAI(model="gemini-1.5-pro", temperature=0.9) # temperature is optional to control the creativity of the response

result = llm.invoke("What is the capital of India and what is the population of that city?")

print(result.content)