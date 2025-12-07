from fastapi import FastAPI
from pydantic import BaseModel
from graph.graph import build_graph
from fastapi.middleware.cors import CORSMiddleware
from langgraph.checkpoint.memory import MemorySaver

app = FastAPI(title="Financial Agent API")

# فعال‌سازی session per-user
checkpointer = MemorySaver()
graph_app = build_graph(checkpointer=checkpointer)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Question(BaseModel):
    thread_id: str
    question: str


@app.post("/ask")
async def ask(data: Question):
    config = {"configurable": {"thread_id": data.thread_id}}
    result = graph_app.invoke(
        {"question": data.question},
        config=config
    )
    return {"result": result}


@app.get("/status/{thread_id}")
async def status(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    state = graph_app.get_state(config)
    return {"state": state.values if state else None}
