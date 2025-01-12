import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
import faiss
import os


# def get_pdf_text():
#     text = ""
#     pdf_reader = PdfReader("src\data2.pdf")
#     number_of_pages = len(pdf_reader.pages)
#     page = pdf_reader.pages[0]
#     text = page.extract_text()
#     return text

def get_pdf_text():
    text = ""
    pdf_reader = PdfReader("src/data2.pdf")
    number_of_pages = len(pdf_reader.pages)

    for page_num in range(number_of_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()  # Append text from each page

    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    for chunk in chunks:
        print(chunk)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    # Save the FAISS vector store to a file
    vectorstore.save_local("vectorstore_index")
    return vectorstore


def load_vectorstore_from_file():
    if os.path.exists("vectorstore_index"):
        # Load the FAISS index from the file
        #   index = faiss.read_index("faiss_index.index")
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(
            "vectorstore_index", embeddings, allow_dangerous_deserialization=True
        )
        return vectorstore
    else:
        return None


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True
            )

def main():
    load_dotenv()
    st.session_state.pred_prompt = ""

    st.set_page_config(page_title="Algo Chat", page_icon=":left_speech_bubble:")
    st.image("assets/img.png")
    st.header("40 Algorithms Every Programmer Should Know Chat:book:")
    with st.spinner("Loading..."):
        # Load document
        far_co_button, far_far_co_button = st.columns([1, 1])
        with far_co_button:
            if st.button(
                "What is Binary Search?", type="primary"
            ):
                st.session_state.pred_prompt = (
                    "What is Binary Search?"
                )

        with far_far_co_button:
            if st.button("What is DFS?", type="primary"):
                st.session_state.pred_prompt = "What is DFS?"

        left_co_button, cent_co_button, right_co_button = st.columns([1, 1, 1])
        with left_co_button:
            if st.button("Give a code example of DFS.", type="primary"):
                st.session_state.pred_prompt = "Give a code example of DFS."

        with cent_co_button:
            if st.button("What is a Linear Regression?", type="primary"):
                st.session_state.pred_prompt = "What is a Linear Regression?"

        with right_co_button:
            if st.button("What is Big O notation?", type="primary"):
                st.session_state.pred_prompt = "What is Big O notation?"

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    user_question = st.text_input(
        "I am here to help you find answers. Please ask a question:"
    )
    if user_question:
        handle_userinput(user_question)

    if st.session_state.pred_prompt:
        handle_userinput(st.session_state.pred_prompt)

    with st.sidebar:
        reset_button_key = "reset_button"
        reset_button = st.button("Reset Chat",key=reset_button_key)
        if reset_button:
          st.session_state.conversation = None
          st.session_state.chat_history = None
        st.subheader("Get Started")
        if st.button("Process"):
            with st.spinner("Hold-tight, Processing"):

                # get pdf text
                raw_text = get_pdf_text()

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                print(text_chunks)

                # create vector store
                vectorstore = load_vectorstore_from_file()
                if vectorstore is None:
                     # create and save vectorstore
                     vectorstore = get_vectorstore(text_chunks)

               #  vectorstore = get_vectorstore(text_chunks)

                # create converstaion chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
if __name__ == "__main__":
    main()
