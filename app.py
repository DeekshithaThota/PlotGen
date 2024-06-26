import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import Agent


load_dotenv()

import os
os.environ['PANDASAI_API_KEY'] = "$2a$10$FWebDEq.KDI6vM7R5PlvhuOjEcOrrkv/AfC1HrtNuZM8ncRLc1R.O"
openai_api_key = os.getenv('PANDASAI_API_KEY')


def chat_with_csv(df,prompt):
    agent = Agent(df)
    result = agent.chat(prompt)
    print(result)
    return result

st.set_page_config(layout='wide')

st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'],encoding='unicode_escape')

if input_csv is not None:

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv)
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            if input_text is not None:
                if st.button("Chat with CSV"):
                    st.info("Your Query: "+input_text)
                    result = chat_with_csv(data, input_text)
                    st.success(result)
