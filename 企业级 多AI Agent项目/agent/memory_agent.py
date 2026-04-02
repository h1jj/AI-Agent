from agent.base_agent import BaseAgent
from memory.shared_memory import SharedMemory

class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="MemoryAgent")
        self.memory = SharedMemory()

    def execute(self, task: str, **kwargs) -> str:
        user_id = kwargs.get("user_id", "default")
        self.memory.add_memory(user_id, task)
        history = self.memory.get_history(user_id)
        return f"已记忆 | 历史对话：{len(history)} 条"