
# Algo Chat: Interactive Knowledge Bot

## Overview
Algo Chat is an interactive chatbot built using Streamlit that provides detailed answers and insights about algorithms and programming concepts. By leveraging LangChain, OpenAI embeddings, and FAISS for vector storage, it enables users to query a PDF document for specific information and engage in meaningful conversations.

## Features
- **PDF Text Extraction**: Extracts and processes text from a PDF document.
- **Text Chunking**: Splits the extracted text into manageable chunks for better processing.
- **Vector Store Creation**: Converts text chunks into embeddings and stores them in a FAISS vector database.
- **Conversational Chain**: Creates a conversational interface powered by OpenAI’s Chat models with retrieval capabilities.
- **Predefined Prompts**: Provides quick access to common algorithmic questions via buttons.
- **Interactive UI**: A user-friendly interface to interact with the bot and retrieve answers.
- **Session Persistence**: Keeps chat history and resets easily when needed.

## How It Works
1. **PDF Processing**: The bot reads a specified PDF file and extracts text from all its pages.
2. **Text Chunking**: The extracted text is divided into smaller chunks using the LangChain `CharacterTextSplitter` to ensure efficient embedding.
3. **Vector Storage**:
   - If a vector store exists, it loads the stored FAISS index.
   - Otherwise, it creates a new vector store from the text chunks and saves it locally.
4. **Conversational Chain**:
   - A conversational retrieval chain is set up with OpenAI’s chat model and the FAISS vector store as the retriever.
5. **User Interaction**:
   - Users can ask questions through a text input box or use predefined buttons for common queries.
   - The chatbot retrieves and displays responses based on the stored embeddings.

## Setup Instructions
### Prerequisites
- Python 3.8+
- Required libraries:
  - `streamlit`
  - `langchain`
  - `PyPDF2`
  - `faiss`
  - `python-dotenv`
  - `openai`

### Installation
1. Clone this repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```
4. Ensure your PDF file is placed in the `src/` directory and named `data2.pdf`.

### Running the App
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the provided URL in your browser to interact with Algo Chat.

## Usage
1. Use the sidebar to process the PDF and initialize the chatbot.
2. Enter your questions in the text input box or use the predefined buttons for quick queries.
3. Reset the chat or reprocess the PDF at any time using the sidebar options.

## File Structure
```
.
├── src/
│   ├── data2.pdf               # The PDF file to be processed
│   └── assets/img.png          # Logo/image for the app
├── app.py                      # Main application code
├── htmlTemplates.py            # Custom HTML templates for chatbot UI
├── requirements.txt            # Required Python libraries
├── .env                        # API keys and environment variables
└── README.md                   # Project documentation (this file)
```

## Future Enhancements
- Add support for multiple PDFs.
- Incorporate advanced search and filtering options.
- Optimize memory usage for handling large documents.
- Expand predefined prompts for more diverse use cases.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI](https://openai.com/)
