from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


llm= GooglePalm(google_api_key=os.environ["google_api_key"], temprature=0.6)
embeddings = HuggingFaceInstructEmbeddings()
vector_database_folder= "vectordb_index"

def create_vector_database():
    loader=CSVLoader(file_path="./codebasics_faqs.csv", source_column="prompt")
    data=loader.load()
    vector_db = FAISS.from_documents(data, embeddings)
    vector_db.save_local(vector_database_folder)


def get_qa_chain():

    vector_db= FAISS.load_local(vector_database_folder,embeddings)
    retriver= vector_db.as_retriever()
    prompt_template= """
    
    PROMPT= Generate your answer using the provided csv document as context and generate the answer
    of the provided question from the text of the “Response” column from the provided text.
    If the provided question is not in the context of provided context just say “I don’t know”.
    Don’t try to make up answer by your own.

    CONTEXT= {context}

    QUESTION= {question}
    
    """


    PROMPT=PromptTemplate(template=prompt_template, input_variables=["question","context"])

    chain = RetrievalQA.from_chain_type(
        chain_type="stuff",
        llm= llm,
        retriever=retriver,
        input_key="query",
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True)
    return chain

# if __name__=="__main__":
#     chain=get_qa_chain()
#     print(chain("Do you provide internship?"))   
