from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import TypedDict,Literal,Optional,Annotated
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  #  through Api
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("write a 5 line of paragraph on nalanda University")
print(result.content)