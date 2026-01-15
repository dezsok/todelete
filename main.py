

import fastapi

app= fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def read_root():
    return {"greeting": "Hello World"}



