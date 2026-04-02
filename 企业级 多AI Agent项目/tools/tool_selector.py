from tools.calc_tool import CalcTool
from tools.search_tool import SearchTool

class ToolSelector:
    def __init__(self):
        self.tools = [
            CalcTool(),
            SearchTool()
        ]

    def select(self, query: str):
        if any(k in query for k in ["计算", "加", "减", "乘", "除"]):
            return CalcTool()
        if any(k in query for k in ["查询", "搜索", "信息", "百科", "新闻"]):
            return SearchTool()
        return None

    def get_tool_names(self):
        return [t.name for t in self.tools]