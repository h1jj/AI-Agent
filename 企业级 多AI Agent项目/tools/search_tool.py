from tools.base_tool import BaseTool
class SearchTool(BaseTool):
    name = "web_search"
    description = "联网搜索工具"

    def run(self, query: str) -> str:
        return f"【联网搜索】{query}\n结果：AI Agent 是企业级智能自动化核心技术。"