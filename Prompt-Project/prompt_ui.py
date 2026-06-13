from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

st.header('Reasearch Tool')

paper_input = st.selectbox("Select Research paper Name",["Select...","Attention is all you need","Bert :Pretraining of bi Directional Transformer","GPT-3:Language Model are few shot leraner","Diffusionmodels Beat GAN on Image Systhesis"])

style_input = st.selectbox("Select EXplaination Style",["Select...","Begginer-Friendly","Technical-Style","Code-Oriented","Mathematical-Style"])

length_input = st.selectbox("Selct Expalination Length",["Select...","Short(1-2 paragraph)","Medium(4-8 Pargraph)","Long(Detail Explaination)"])

# load template json
template =load_prompt('template.json')

# # # fill placeholder
# prompt = template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })


token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  #  through Api
    task="text-generation",
    huggingfacehub_api_token=token,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

if st.button('Summarize'):
    chain = template | model  # create a chain
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})
    st.write(result.content)