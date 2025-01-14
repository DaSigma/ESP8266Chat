Algo Chat: Interactive Knowledge Bot

Overview

Algo Chat is an interactive chatbot built using Streamlit that provides detailed answers and insights about algorithms and programming concepts. By leveraging LangChain, OpenAI embeddings, and FAISS for vector storage, it enables users to query a PDF document for specific information and engage in meaningful conversations.

Features

PDF Text Extraction: Extracts and processes text from a PDF document.

Text Chunking: Splits the extracted text into manageable chunks for better processing.

Vector Store Creation: Converts text chunks into embeddings and stores them in a FAISS vector database.

Conversational Chain: Creates a conversational interface powered by OpenAI’s Chat models with retrieval capabilities.

Predefined Prompts: Provides quick access to common algorithmic questions via buttons.

Interactive UI: A user-friendly interface to interact with the bot and retrieve answers.

Session Persistence: Keeps chat history and resets easily when needed.

How It Works

PDF Processing: The bot reads a specified PDF file and extracts text from all its pages.

Text Chunking: The extracted text is divided into smaller chunks using the LangChain CharacterTextSplitter to ensure efficient embedding.

Vector Storage:

If a vector store exists, it loads the stored FAISS index.

Otherwise, it creates a new vector store from the text chunks and saves it locally.

Conversational Chain:

A conversational retrieval chain is set up with OpenAI’s chat model and the FAISS vector store as the retriever.

User Interaction:

Users can ask questions through a text input box or use predefined buttons for common queries.

The chatbot retrieves and displays responses based on the stored embeddings.

Setup Instructions

Prerequisites

Python 3.8+

Required libraries:

streamlit

langchain

PyPDF2

faiss

python-dotenv

openai

Installation

Clone this repository.

git clone <repository-url>
cd <repository-directory>

Install the required Python libraries:

pip install -r requirements.txt

Add your OpenAI API key to a .env file:

OPENAI_API_KEY=your_openai_api_key

Ensure your PDF file is placed in the src/ directory and named data2.pdf.

Running the App

Start the Streamlit app:

streamlit run app.py

Open the provided URL in your browser to interact with Algo Chat.

Usage

Use the sidebar to process the PDF and initialize the chatbot.

Enter your questions in the text input box or use the predefined buttons for quick queries.

Reset the chat or reprocess the PDF at any time using the sidebar options.

File Structure

.
├── src/
│   ├── data2.pdf               # The PDF file to be processed
│   └── assets/img.png          # Logo/image for the app
├── app.py                      # Main application code
├── htmlTemplates.py            # Custom HTML templates for chatbot UI
├── requirements.txt            # Required Python libraries
├── .env                        # API keys and environment variables
└── README.md                   # Project documentation (this file)

Future Enhancements

Add support for multiple PDFs.

Incorporate advanced search and filtering options.

Optimize memory usage for handling large documents.

Expand predefined prompts for more diverse use cases.