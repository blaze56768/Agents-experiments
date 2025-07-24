import datasets
from llama_index.core.schema import Document
from llama_index.core.tools import FunctionTool
from llama_index.retrievers.bm25 import BM25Retriever


class GuestInfoRetrieverTool:
    def __init__(self, docs):
        # Filter out any empty documents
        valid_docs = [doc for doc in docs if doc.text and doc.text.strip()]
        
        self.retriever = BM25Retriever.from_defaults(nodes=valid_docs)

        def query_guest_info(query: str) -> str:
            results = self.retriever.get_relevant_documents(query)
            if results:
                return "\n\n".join([doc.text for doc in results[:3]])
            else:
                return "No matching guest information found."

        # Create FunctionTool instance
        self.tool = FunctionTool.from_defaults(
            fn=query_guest_info,
            name="guest_info",
            description="Retrieves detailed information about gala guests based on their name or relation."
        )

    def get_tool(self):
        return self.tool


def load_guest_dataset():
    # Load the dataset
    guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")

    # Convert dataset entries into Document objects
    docs = [
        Document(
            text="\n".join([
                f"Name: {guest['name']}",
                f"Relation: {guest['relation']}",
                f"Description: {guest['description']}",
                f"Email: {guest['email']}"
            ]),
            metadata={"name": guest["name"]}
        )
        for guest in guest_dataset
    ]

    return GuestInfoRetrieverTool(docs).get_tool()










# # from smolagents import Tool
# # from langchain_community.retrievers import BM25Retriever
# # from langchain.docstore.document import Document
# import datasets
# from llama_index.core.schema import Document
# from llama_index.core.tools import FunctionTool
# from llama_index.retrievers.bm25 import BM25Retriever


# class GuestInfoRetrieverTool(FunctionTool):
#     name = "guest_info_retriever"
#     description = "Retrieves detailed information about gala guests based on their name or relation."
#     inputs = {
#         "query": {
#             "type": "string",
#             "description": "The name or relation of the guest you want information about."
#         }
#     }
#     output_type = "string"

#     def __init__(self, docs):
#         self.is_initialized = False
#         self.retriever = BM25Retriever.from_defaults(nodes=docs)
       

#     def forward(self, query: str):
#         results = self.retriever.get_relevant_documents(query)
#         if results:
#             return "\n\n".join([doc.text for doc in results[:3]])
#         else:
#             return "No matching guest information found."


# def load_guest_dataset():
#     # Load the dataset
#     guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")

#     # Convert dataset entries into Document objects
#     docs = [
#         Document(
#             page_content="\n".join([
#                 f"Name: {guest['name']}",
#                 f"Relation: {guest['relation']}",
#                 f"Description: {guest['description']}",
#                 f"Email: {guest['email']}"
#             ]),
#             metadata={"name": guest["name"]}
#         )
#         for guest in guest_dataset
#     ]

#     # Return the tool
#     return GuestInfoRetrieverTool(docs)



