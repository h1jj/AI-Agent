from agent.base_agent import BaseAgent

class UserAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="UserAgent")

    def execute(self, task: str, **kwargs) -> str:
        prompt = f"""你是用户意图Agent，请清晰理解用户需求：
用户问题：{task}
返回简洁的意图总结。"""
        return self.llm.invoke(prompt).content