from abc import ABC, abstractmethod
# 1.  OpenAI 导入
# from langchain_openai import ChatOpenAI
# 2. 改用本地 Ollama 模型（不需要 API Key，不需要联网）
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        # 3. 连接本地模型
        self.llm = ChatOllama(
            model="deepseek-r1:1.5b",  # 确保你已经用 `ollama pull` 下载了这个模型
            base_url="http://localhost:11434",
            temperature=float(os.getenv("TEMPERATURE", 0.1)),
            max_tokens=int(os.getenv("MAX_TOKENS", 4096))
        )
    @abstractmethod
    def execute(self, task: str, **kwargs) -> str:
        pass