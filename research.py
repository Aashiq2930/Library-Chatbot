from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.chains import ConversationChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

def re():
    st.title("Clara: AI-Assisted Library Chatbot📚")
    with st.sidebar:
        st.info("Introducing our Library Assistant Chatbot - your friendly and knowledgeable companion for all your research needs! Powered by advanced AI technology, our chatbot is designed to help you find books, articles, and resources quickly and efficiently. Whether you're looking for recommendations, assistance with citations, or simply seeking information, our library assistant is here to provide prompt and personalized support. Say hello to hassle-free research with our Library Assistant Chatbot!")
    def rebot():

        

        llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.2)
        
        if "messages" not in st.session_state:
                    st.session_state.messages = [{'role':'assistant', 'content':'Hey, This is Clara. How may I assist you today?'}]
        for message in st.session_state.messages:
                    with st. chat_message(message["role"]):
                        st. write (message["content"])

        # if 'buffer_memory' not in st.session_state:
        #     st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3, return_messages=True)

        # system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the
        #     question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say 'I don't know'""")
        
        # human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")
        template = """You are student helper chatbot for research purpose be friendly and interactive and read the previous chat history .

        {chat_history}
        Human: {human_input}
        Chatbot:
        """

        prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template)
        memory = ConversationBufferMemory(memory_key="chat_history")
        
        conversation = LLMChain(memory=memory,
            prompt=prompt, llm=llm, verbose=True)
        
        qu=st.chat_input("Ask Your Question",key=f'post_{len(st.session_state.messages)}')
        if qu:
            st. session_state. messages.append({"role": "user","content": qu})
            with st.chat_message ("user"):
                st.write(qu)
        
        if st.session_state.messages[-1]['role']!= 'assistant':
                with st.chat_message("assistant"):
                    with st.spinner("Thinking🤔..."):
                        response = conversation.run(qu)
                    st. write(response)
                    st. session_state.messages. append(
                                {"role": "assistant",
                                "content": response})
    rebot()