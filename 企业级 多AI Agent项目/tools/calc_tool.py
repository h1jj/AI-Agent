from tools.base_tool import BaseTool

class CalcTool(BaseTool):
    name = "calculator"
    description = "数学计算工具"

    def run(self, query: str) -> str:
        try:
            expr = query.replace("计算", "").replace(" ", "")
            return f"计算结果：{eval(expr)}"
        except:
            return "计算失败"