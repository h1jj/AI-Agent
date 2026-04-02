from tools.calc_tool import CalcTool
from tools.search_tool import SearchTool
from tools.tool_selector import ToolSelector

def test_calc_tool():
    calc = CalcTool()
    res = calc.run("计算 10+20")
    print("计算工具测试:", res)
    assert "30" in res

def test_search_tool():
    search = SearchTool()
    res = search.run("查询AI")
    print("搜索工具测试:", res)
    assert len(res) > 0

def test_tool_selector():
    selector = ToolSelector()
    tool1 = selector.select("计算 5*5")
    tool2 = selector.select("搜索天气")
    print("工具选择器测试:", tool1, tool2)
    assert tool1 is not None

if __name__ == "__main__":
    test_calc_tool()
    test_search_tool()
    test_tool_selector()
    print("✅ 所有工具测试通过")