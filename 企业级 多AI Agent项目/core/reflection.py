from langchain_ollama import ChatOllama
import os

class Reflector:
    def __init__(self):
        self.llm = ChatOllama(
            model="deepseek-r1:1.5b",
            base_url="http://localhost:11434",
            temperature=0.0
        )

    def reflect(self, task: str, result: str) -> str:
        prompt = f"""你是反思Agent，检查结果是否准确、完整、无错误。
问题：{task}
结果：{result}
请输出修正后的最终结果。"""
        return self.llm.invoke(prompt).content