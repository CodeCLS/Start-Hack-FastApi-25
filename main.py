
import openai_repo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    output = openai_repo.OpenaiRepo().send_completion_request("Hello")
    print(output)
    if output is None:
        return {"Dumb"}
    try:
        return {"message": "Hello World" + output}
    except Exception as e:
        print(e)
        return {"DUmber"}