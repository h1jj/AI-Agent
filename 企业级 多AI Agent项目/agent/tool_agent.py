from agent.base_agent import BaseAgent
from tools.calc_tool import CalcTool
from tools.search_tool import SearchTool

class ToolAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ToolAgent")
        self.calc = CalcTool()
        self.search = SearchTool()

    def execute(self, task: str, **kwargs) -> str:
        if any(k in task for k in ["计算", "加", "减", "乘", "除"]):
            return self.calc.run(task)
        if any(k in task for k in ["查询", "搜索", "查一下", "百科"]):
            return self.search.run(task)
        return "无需工具，直接回答：" + self.llm.invoke(task).content