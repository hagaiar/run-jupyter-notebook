from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import awswrangler as wr

import papermill as pm

app = FastAPI()

class Nb_params(BaseModel):
    limit: int = 1000
    country_limit: int = 15

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/activate_python_notebook")
def activate_python_notebook(parameters_for_notebook: Nb_params
    , notebook_source: str='s3://aiola-469190457957-h-playground/misc/num_flights_by_country.ipynb'
    , notebook_target: str='s3://aiola-469190457957-h-playground/misc/jupyter_notebooks_outputs/num_of_flights_by_country.ipynb'):

    dict_of_params = dict(parameters_for_notebook)

    pm.execute_notebook(
        notebook_source,
        notebook_target,
        parameters=dict(limit=dict_of_params['limit']
            , country_limit=dict_of_params['country_limit'])
    )

    wr.download(path='s3://aiola-469190457957-h-playground/images/flights_by_country.png', local_file='flights_by_country.png')
    return FileResponse('flights_by_country.png')
