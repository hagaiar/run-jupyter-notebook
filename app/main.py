from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("activate_python_notebook")
def activate_python_notebook(notebook_source: str, notebook_target: str, parameters: list):
    # TODO: activate the notebook using papermill and return the output

    return None
