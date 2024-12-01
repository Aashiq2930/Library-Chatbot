from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain
import os 
from dotenv import load_dotenv
load_dotenv()

db_file_path = 'FAISS_Index'
embeddings = HuggingFaceEmbeddings()

def creation_of_vectorDB_in_local(loader):
    data = loader.load()
    db = FAISS.from_documents(data, embeddings)
    db.save_local(db_file_path)

def creation_FAQ_chain():
    db=FAISS.load_local(db_file_path, embeddings,allow_dangerous_deserialization = True)
    retriever =db.as_retriever(score_threshold=0.7)
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.2)
    
    prompt_temp = """Given the following context and a question, generate an answer based on this context only. 
            The source document contains a CSV file with two columns: Genre of Book and Aisle & Direction. 
            Each row represents a genre of book along with its corresponding aisle and direction in the library.
            Now, using the provided context and question, generate an answer based on the information provided in the context section. 
            For questions related to location or directions, provide only the relevant aisle, shelves, and direction information without including the genre.
            If the user says "thanks," "thank you," "ok," or similar expressions, respond politely and confirm your assistance.
            CONTEXT: {context}
            QUESTION: {question}"""


    PROMPT = PromptTemplate(template=prompt_temp, input_variables=["context", "question"])
    chain = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff", 
                                        retriever=retriever, 
                                        input_key="query", 
                                        return_source_documents=False,
                                        chain_type_kwargs={"prompt" : PROMPT})
    return chain


def rechatbot(q):
    llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.4)
    template = """As the library book description provider, I'll furnish detailed information about the book, including its title, 
    author's name, topics covered, reviews, and additional insights from a student's perspective. 
    Additionally, I'll include a rating and recommendations for similar books .

    {topic}
    """

    prompt = PromptTemplate(
    input_variables=["topic"], template=template
    )


    # temp="""You are the library book description giver you give detail of the book including name author name what are the topics involved in that book and reviews also"""
    # tweet_prompt = PromptTemplate.from_template(" {topic}.")



    tweet_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    res=tweet_chain.run(topic=q)
    return res


