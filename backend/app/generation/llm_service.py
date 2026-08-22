from abc import ABC, abstractmethod

import ollama


class BaseLLMService(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class OllamaLLMService(BaseLLMService):

    def __init__(self, model: str = "qwen2.5:3b"):
        self.model = model

    def generate(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


llm_service = OllamaLLMService()