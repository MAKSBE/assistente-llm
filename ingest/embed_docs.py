from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import chromadb

loader = DirectoryLoader("./docs", glob="**/*.*")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
chunks = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings()
client = chromadb.HttpClient(host="chroma", port=8000)  # Conecta no serviço ChromaDB do container
collection = client.get_or_create_collection(name="dotnet-docs")

for chunk in chunks:
    collection.add(
        documents=[chunk.page_content],
        metadatas=[chunk.metadata],
        ids=[chunk.metadata.get("source", str(hash(chunk.page_content)))]
    )

print("Documentação indexada com sucesso!")
