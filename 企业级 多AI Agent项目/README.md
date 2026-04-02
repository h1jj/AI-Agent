# 多Agent协同 AI 项目（本地部署版）
基于 LangChain 构建，支持多Agent自动分工协作。

## 功能
- UserAgent：意图理解
- ToolAgent：工具调用（计算、搜索）
- MemoryAgent：共享记忆
- SchedulerAgent：任务调度
- Reflection：反思修正

## 启动
1. 官网安装ollama，下载ollama模型：ollama pull deepseek—r1:1.5b
2. 安装依赖：pip install -r requirements.txt
3. 运行：uvicorn main:app --reload
4. 打开浏览器访问 http://localhost:8000/static/index.html