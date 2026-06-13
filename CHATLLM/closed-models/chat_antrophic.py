from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-2", temperature=0.9)

result = llm.invoke("What is the capital of India and what is the population of that city?")
print(result.content)