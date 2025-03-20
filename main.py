
import openai_repo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    output = openai_repo.OpenaiRepo().send_completion_request("Hello")
    try:
        return {"message": "Hello World" + output}
    except:
        return {"message": "Hello World"}
