from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query,
        chunks,
        top_k=3,
        min_score=0.0
    ):

        if not chunks:
            return []

        pairs = [
            [query, chunk.content]
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(chunks, scores),
            key=lambda item: float(item[1]),
            reverse=True
        )

        filtered = [
            (chunk, score)
            for chunk, score in ranked
            if float(score) >= min_score
        ]

        return filtered[:top_k]


reranker = Reranker()