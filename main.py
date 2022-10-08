import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"welcome"}}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
