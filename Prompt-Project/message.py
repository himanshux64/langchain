from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  #  through Api
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are Helpful Assistance'),
    HumanMessage(content='Tell me about Langchain ')
]

result= model.invoke(messages)

messages.append(AIMessage(result.content))
print(messages)