from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agent.scheduler_agent import SchedulerAgent
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
agent = SchedulerAgent()
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    reply = agent.run(req.message)
    return {"reply": reply}
@app.get("/")
def home():
    return {"message": "访问 http://localhost:8000/static/index.html 进入聊天界面"}