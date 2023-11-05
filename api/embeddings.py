import openai
import pymongo

from constants import OPENAI_API_KEY


def embed_text(text: str, model: str = "text-embedding-ada-002") -> list[float]:
    """Embeds `text` using `model`."""
    text = text.replace("\n", " ")
    return openai.Embedding.create(
        input=[text],
        model=model,
        api_key=OPENAI_API_KEY,
    )[
        "data"
    ][0]["embedding"]


def vector_search(
    query: str,
    collection: pymongo.collection.Collection,
    index,
    path,
    candidates: int = 100,
    limit: int = 4,
    embeddings_model: str = "text-embedding-ada-002",
) -> list[str]:
    """Finds the most similar documents to `query` in `collection` using
    vector search.
    """
    query_vector = embed_text(query, embeddings_model)
    results = collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": query_vector,
                    "path": path,
                    "numCandidates": candidates,
                    "limit": limit,
                    "index": index,
                }
            }
        ]
    )
    return [result["text"] for result in results]
