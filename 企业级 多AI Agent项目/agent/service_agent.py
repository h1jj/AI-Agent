from agent.base_agent import BaseAgent

class ServiceAgent(BaseAgent):
    def __init__(self):
        super().__init__("ServiceAgent")

    def execute(self, question: str, **kwargs):
        prompt = f"""
你是企业智能客服，礼貌、专业、简洁回答用户问题：
问题：{question}
请用客服语气回答。
"""
        return self.llm.invoke(prompt).content