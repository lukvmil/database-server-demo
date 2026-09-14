import uvicorn
from fastapi import FastAPI, Request


app = FastAPI(title="Database Server Demo")
db = {}

@app.post("/set")
def set_key(request: Request):
    db.update(request.query_params)
    
@app.get("/get")
def get_key(key: str):
    return db.get(key)

server = uvicorn.Server(
    config=uvicorn.Config(
        app=app,
        host="localhost",
        port=4000
    )
)

if __name__ == "__main__":
    try:
        server.run()
    except KeyboardInterrupt:
        pass