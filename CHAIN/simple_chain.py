from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

prompt = PromptTemplate(
    template='Generate 5 python code that using Production {code}',
    input_variables=['code']
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  #  through Api
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'code':'pandas'})

print(result)


# get pipeline draw
# r =chain.get_graph()
# print(r.print_ascii())