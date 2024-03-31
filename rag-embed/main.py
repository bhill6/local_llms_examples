import gradio as gr
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter


# We don't want to have to rebuild the embedding for every question
# So cache the retriever here once it's built
retriever = None
cached_urls = None


def process_input(urls, question):
    global retriever, cached_urls
    # initialize the chat model
    model_local = ChatOllama(model="mistral")

    # Clear the retriever to build a new one if the cached_urls change
    if cached_urls != urls:
        retriever = None

    # create a new retriever if needed
    if retriever is None:
        print("rebuilding database")
        cached_urls = urls
        # Convert string of URLs to list
        urls_list = urls.split("\n")
        # fetch documents from urls
        docs = [WebBaseLoader(url).load() for url in urls_list]
        docs_list = [item for sublist in docs for item in sublist]
        # split documents into chunks
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
        doc_splits = text_splitter.split_documents(docs_list)
        # store document chunks in embedding database
        # the embedding model manages how the embedding tokenization is managed
        vectorstore = Chroma.from_documents(
            documents=doc_splits,
            collection_name="rag-chroma",
            embedding=OllamaEmbeddings(model='nomic-embed-text'),
        )
        retriever = vectorstore.as_retriever()

    # Use a prompt template that tries to restrict the algorithm to mostly draw 
    # from the embedded context in it's response.
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | after_rag_prompt
            | model_local
            | StrOutputParser()
    )
    print("Submitting prompt + context to model")
    return after_rag_chain.invoke(question)


# Define and run Gradio interface
iface = gr.Interface(fn=process_input,
                     inputs=[gr.Textbox(label="Enter URLs separated by new lines"), gr.Textbox(label="Question")],
                     outputs="text",
                     title="Document Query with Ollama",
                     description="Enter URLs and a question to query the documents.")
iface.launch(server_name="0.0.0.0", server_port=7861)