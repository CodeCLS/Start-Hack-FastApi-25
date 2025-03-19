
import openai_repo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    output = openai_repo.OpenaiRepo().send_completion_request("Hello")
    return {"message": "Hello World" + output}