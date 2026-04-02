from agent.scheduler_agent import SchedulerAgent

agent = SchedulerAgent()

def test_chat():
    res = agent.run("你好")
    print("测试对话:", res)

def test_calc():
    res = agent.run("计算 10+20")
    print("测试计算:", res)

def test_search():
    res = agent.run("帮我查询AI发展")
    print("测试搜索:", res)

if __name__ == "__main__":
    test_chat()
    test_calc()
    test_search()
    print("✅ 所有测试通过")