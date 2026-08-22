from app.generation.llm_service import llm_service


prompt = """
You are a helpful assistant.

Answer this question briefly:

What is retrieval-augmented generation?
"""

response = llm_service.generate(prompt)

print("\nLLM RESPONSE")
print(response)