from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import AIEngine
from prompts import get_system_prompt
app = FastAPI(title="Student LinkedIn & Resume Assistant API")
# Enable CORS so your Chrome Extension can talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
engine = AIEngine()
class RequestData(BaseModel):
    task: str
    user_input: str
    session_memory: dict = {}
@app.post("/api/assistant")
async def handle_request(data: RequestData):
    try:
        system_prompt = get_system_prompt(data.task, data.session_memory)
        response = engine.generate_response(system_prompt, data.user_input)
        return {"success": True, "result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)