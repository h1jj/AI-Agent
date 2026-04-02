import time
from agent.user_agent import UserAgent
from agent.tool_agent import ToolAgent
from agent.memory_agent import MemoryAgent
from agent.service_agent import ServiceAgent
from core.reflection import Reflector
from tools.tool_selector import ToolSelector
from core.monitor import AgentMonitor
from core.security import SecurityManager

class SchedulerAgent:
    def __init__(self):
        self.user_agent = UserAgent()
        self.tool_agent = ToolAgent()
        self.memory_agent = MemoryAgent()
        self.service_agent = ServiceAgent()
        self.reflector = Reflector()
        self.tool_selector = ToolSelector()
        self.monitor = AgentMonitor()
        self.security = SecurityManager()

    def run(self, task: str, user_id="default"):
        self.monitor.track_request()
        start = time.time()

        intent = self.user_agent.execute(task)
        tool = self.tool_selector.select(task)
        tool_result = tool.run(task) if tool else "无需工具"
        mem_info = self.memory_agent.execute(task, user_id=user_id)
        service_reply = self.service_agent.execute(task)
        final = self.reflector.reflect(task, tool_result or service_reply)

        self.monitor.track_latency(time.time() - start)
        if tool: self.monitor.track_tool_use(tool.name)

        return f"""
【客服回复】{service_reply}
【意图】{intent}
【记忆】{mem_info}
【工具】{tool_result}
【最终】{final}
"""