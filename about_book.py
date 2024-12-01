import streamlit as st
from Base import rechatbot


def abtbook():
    st.title("Clara: AI-Assisted Library Chatbot📚")
            
    def research():
        with st.sidebar:
            st.info("Give The name of the book and the author name to know about you books and enjoy")
        
        if "messages" not in st.session_state:
            st.session_state.messages = [{'role':'assistant', 'content':'Hey, This is Clara. How may I assist you today?'}]
        for message in st.session_state.messages:
            with st. chat_message(message["role"]):
                st. write (message["content"])
            
        
        topic = st.chat_input("Enter the book Name ")
        
        if topic:
            st. session_state. messages.append({"role": "user","content": topic})
            with st.chat_message ("user"):
                st.write(topic)
            
            
        if st.session_state.messages[-1]['role']!= 'assistant':
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking🤔..."):
                            repo=rechatbot(topic)
                            
                        st. write(repo)
                        st. session_state.messages. append(
                            {"role": "assistant",
                            "content": repo})
    research()