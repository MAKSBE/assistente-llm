import chromadb

def get_relevant_docs(query):
    client = chromadb.HttpClient(host="chroma", port=8000)
    collection = client.get_or_create_collection(name="dotnet-docs")
    results = collection.query(query_texts=[query], n_results=2)
    return results['documents'][0] if results['documents'] else []
