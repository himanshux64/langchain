from langchain_openai import OpenAI
from  dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal
import os

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

# result =  llm.invoke("What is the capital of India and what is the population of that city?")
# print(result)


# Schema

class Review(BaseModel):
    key_themes :list[str]= Field(description="Write down all the key theme discussed in the review in a list")
    summary : str = Field(description="A brief summary of review")
    sentiment :Literal['pos','cos'] = Field("return sentiment reivew either negative or positive and Neutral")

structured_model = llm.with_structured_output(Review)  # Only Closed Source model provide this method

result = structured_model.invoke("""
The Samsung Galaxy J2 is a budget Android smartphone designed for everyday use. It features a compact display, basic camera functions, and support for common apps such as messaging, browsing, and social media. Its affordable price made it popular among users looking for a simple smartphone. A small device doing its best in a world where phones increasingly resemble glass paving stones
""")

print(result)
