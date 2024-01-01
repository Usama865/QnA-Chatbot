# Chatbot App using Language Models (LLM)

## Overview

This repository contains code for a Chatbot application that utilizes Language Models (LLMs) to generate responses to user queries. The application is designed to provide answers based on a given context using a combination of GooglePalm LLM, HuggingFaceInstructEmbeddings, and FAISS for vector storage and retrieval.

## Components

### 1. Language Model (LLM)

The code utilizes the GooglePalm LLM, which requires a Google API key provided through environment variables. The temperature parameter for the model is set to 0.6 for generating responses.

### 2. Document Loading

The application loads data from a CSV file named "codebasics_faqs.csv" using the CSVLoader from langchain.document_loaders. The "prompt" column from the CSV file is used as the source of the context for the chatbot.

### 3. Embeddings

HuggingFaceInstructEmbeddings is employed to convert the textual data into vector embeddings.

### 4. Vector Storage

The vector storage is handled by the FAISS library. The application creates a vector database from the loaded CSV data and saves it locally for efficient retrieval.

### 5. Question-Answer Chain

The RetrievalQA chain is constructed using the vector database, GooglePalm LLM, and a prompt template. The prompt template defines how the question and context should be presented to the model for generating responses.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Set up the required environment variables, including the Google API key, using a dotenv file.
3. Run the `create_vector_database` function to generate and save the vector database.
4. Uncomment the last few lines in the code to instantiate the QA chain and query the chatbot with a specific question.

Please note that the provided prompt template instructs the chatbot to generate an answer based on the context and question provided. If the question is not within the context, the chatbot responds with "I don't know" without attempting to make up an answer. Use the Sample.txt file in the repository for sample questions.

## Note
I am still working on this project to make it more dynamic. I am working on to make it a pdf reader type app, so that a user can upload any pdf(s) and the app will read the pdf page by page and the user can as questions to the app based on the context of the provided pdf(S).
SO STAY TUNE FOR UPDATES :)

Feel free to customize the code and prompt template according to your specific use case.
