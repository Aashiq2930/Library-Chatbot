from langchain_community.document_loaders import CSVLoader
import tempfile
import streamlit as st
from Base import creation_FAQ_chain,creation_of_vectorDB_in_local

def guide():
    st.title("Clara: AI-Assisted Library Chatbot📚")

    def csv_loader(tmp_file_path):
                loader=CSVLoader(file_path=tmp_file_path)

                return loader
    def main_():
                # st.set_page_config(page_title="Clara",page_icon="😈",layout="wide")
                # st.title("Clara: AI-Assisted Library 📚")

                with st.sidebar:
                    st.title("Settings")
                    st.markdown('---')
                    st.subheader('Upload Your CSV File')
                    doc=st.file_uploader("Upload your CSV file and Click Process",'csv')

                    if st.button("Process"):
                        with st.spinner("Processing"):
                            if doc is not None:
                                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                                    tmp_file.write(doc.getvalue())
                                    tmp_file_path = tmp_file.name
                        
                                    st.success(f'File {doc.name} is successfully saved!')
                                
                                load=csv_loader(tmp_file_path)
                                creation_of_vectorDB_in_local(load)
                                st.success("Process Done")
                            else:
                                st.error("❗️Please Upload Your File❗️")
                    
                if "messages" not in st.session_state:
                    st.session_state.messages = [{'role':'assistant', 'content':'Hey, This is Clara. How may I assist you today?'}]
                for message in st.session_state.messages:
                    with st. chat_message(message["role"]):
                        st. write (message["content"])

                query=st.chat_input("Ask the Question")
                if query:
                    st. session_state. messages.append({"role": "user","content": query})
                    with st.chat_message ("user"):
                        st.write(query)
                    
                    
                    

                if st.session_state.messages[-1]['role']!= 'assistant':
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking🤔..."):
                            ans=creation_FAQ_chain()
                            result=ans(query)
                            a=result["result"]
                        st. write(a)
                        st. session_state.messages. append(
                            {"role": "assistant",
                            "content": a})
    
    main_()