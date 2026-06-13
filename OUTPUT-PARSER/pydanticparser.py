from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import TypedDict,Literal,Optional,Annotated
from langchain_core.output_parsers import PydanticOutputParser
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

class Person(BaseModel):
    name : str = Field(description='Name of the Person')
    age : int = Field(description='Age of the Person')
    city : str = Field(description=' NAme of City that belongs to')

parser = PydanticOutputParser(
    pydantic_object=Person
)

 
template = PromptTemplate(
    template='write a detailed report on data name ,age and city of fiction {place} person \n {format_instruction}',
    input_variables=['palce'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'place': 'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
