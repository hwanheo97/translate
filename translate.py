# -*- coding: utf-8 -*-
"""5_6_번역_서비스_만들기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ADNbii_zjFODtge-jCYRm3MAY4kreREB
"""

#langchain==0.0.350에서 dependency 오류가 발생하여 기존 langchanin 삭제
#!pip3 uninstall -y langchain

#langchain==0.0.350에서 dependency 오류가 발생하여 langchanin 최신 버전으로 설치
#!pip install langchain

#langchain-community 역시 재설치
#!pip install -U langchain-community

#!pip install streamlit==1.29.0

#!pip install openai==0.28.1

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

import os
os.environ["OPENAI_API_KEY"] = st.secrets["auth_api_key"] #openai 키 입력

# 웹페이지에 보여질 내용
langs = ["Korean", "Japanese", "chinese", "English"]  #번역을 할 언어를 나열
left_co, cent_co,last_co = st.columns(3)

#웹페이지 왼쪽에 언어를 선택할 수 있는 라디오 버튼
with st.sidebar:
     language = st.radio('번역을 원하는 언어를 선택해주세요.:', langs)

st.markdown('### 언어 번역 서비스예요~')
prompt = st.text_input('번역을 원하는 텍스트를 입력하세요')  #사용자의 텍스트 입력

trans_template = PromptTemplate(
    input_variables=['trans'],
    template='Your task is to translate this text to ' + language + 'TEXT: {trans}'
)  #해당 서비스가 번역에 대한 것임을 지시

#momory는 텍스트 저장 용도
memory = ConversationBufferMemory(input_key='trans', memory_key='chat_history')

llm = OpenAI(model_name="gpt-4", temperature=0)
trans_chain = LLMChain(llm=llm, prompt=trans_template, verbose=True, output_key='translate', memory=memory)

# 프롬프트(trans_template)가 있으면 이를 처리하고 화면에 응답을 작성
if st.button("번역"):
    if prompt:
        response = trans_chain({'trans': prompt})
        st.info(response['translate'])

