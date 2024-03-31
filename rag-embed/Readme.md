# Retrieval Augmented Generation 

Retrieval Augmented Generation (RAG) relies on the ability of LLMs to summarize and answer questions about a specific limited context, such as a document or set of documents. This limits the likelihood of the LLM providing incorrect information, since it will generate the response based on the context submitted.

Data preparation is important, in my experience. It seems that a FAQ-like format is easier for the LLM to summarize and answer questions from, and tables are the most difficult. It might be useful to pre-process the documents for easier summarization, such as splitting on Markdown headers, providing a text summary of tabular data and graphs, and ensuring that the language syntax is clear. 

## Preparation
1. Fetch documents from URLs
2. Flatten documents into list of text-like data
3. Split data into smaller chunks (with overlaps)
4. Convert chunks into embedding tokens
5. Store tokens in vector database
6. Create retriever for vector database

## Prompt
```
Answer the question based only on the following context:
{context}

Question: {question}
```

## Usage
7. Fetch relevant embeddings from vector database for input question
8. Submit prompt, context, and input question to LLM
9. Profit

