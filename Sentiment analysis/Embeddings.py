
from setuptools import setup
from llama_index import StorageContext, load_index_from_storage, SimpleDirectoryReader, VectorStoreIndex
import fpdf
import openai 

AppName = "com.zenithBank.eazymoney"
Store = "PlayStore"

Prompt = "Give me the 10 reviews to this app that contain the most negative sentiment with a reason that the app specifically is causing this sentiment from the last 6 months (January to June of 2023). If the comments were made on a date before the last 6 months from January to June of 2023, do not add the comments and just provide me with a list of whatever comments are available in that time range that have the most negative sentiment. Provide me the 10 reviews to this app that contain the most positive sentiment with a reason that the app specifically is causing this sentiment from the last 6 months (January to June of 2023). If the comments were made on a date before the last 6 months from January to June of 2023, do not add the comments and just provide me with a list of whatever comments are available in that time range that have the most positive sentiment. Also write for me the 3 biggest actionable changes to the functionality of the app that should be made to the app with the percentage of all the reviews in the whole file that mention this change based on reviews from the last 6 months only (January to June of 2023). Also write for me the 3 biggest actionable changes to the UI/UX of the app that should be made to the app with the percentage of all the reviews in the whole file that mention this change based on reviews from the last 6 months (January to June of 2023)."

def Embeddings(AppName, Prompt):

    openai.api_key= "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"

    try:
        print("Attempting to load index from storage")
        storage_context = StorageContext.from_defaults(persist_dir="./Storage-" + Store + "-" + AppName)
        index = load_index_from_storage(storage_context)
        print("Loaded index from storage")
    except:
        print("Failed to load index from storage, creating new index")
        documents = SimpleDirectoryReader(input_files=["Comments-" + Store + "-" +
                                                        AppName + ".pdf"]).load_data()
        index = VectorStoreIndex.from_documents(documents)
        print("Created new index")

    query_engine = index.as_query_engine()
    response = query_engine.query(Prompt)

    pdf2 = fpdf.FPDF(format='letter')
    pdf2.add_page()
    pdf2.set_font("Arial", "",  size=10)

    print(response)

    text = str(response)
    review = text.encode('latin-1', 'replace').decode('latin-1')
    pdf2.write(12, review) 
    pdf2.ln()

    pdf2.output("Analysis-" + Store + "-" + AppName + ".pdf")

    index.storage_context.persist(persist_dir="./Storage-" + Store + "-" + AppName)

Embeddings(AppName, Prompt)