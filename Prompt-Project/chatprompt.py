from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage

chat_template = ChatPromptTemplate([
    ('system','You are helpfull {domain} expert'),
    ('human','Explain in simple terms ,What is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'LBW'})
print(prompt)