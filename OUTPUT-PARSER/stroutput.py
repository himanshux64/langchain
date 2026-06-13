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

tem1 =PromptTemplate(
    template='write a 5 line summaries on following text. /n {text}',
    input_variables=['text']
)

# 2nd Prompt 
temp2 = PromptTemplate(
    template='write a detailed report on {text}  No fluff only pure wisdom',
    input_variables=['text']
)

#-------------------------------------------------------------------
# prompt = tem1.invoke({'text':'why am i Athiest'})

# result = model.invoke(prompt)

# promt1= temp2.invoke({'topic':result.content})

# res = model.invoke(promt1)

# print(res.content)
#----------------------------------------------------------------

##################################################################################
############ STR OUTPUT parser
###################################

parser = StrOutputParser()

chain = tem1 | model | parser |temp2 | model | parser

resy =chain.invoke({'text':'black hole'})

print(resy)
#################################################################