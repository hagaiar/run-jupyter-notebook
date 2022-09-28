FROM python:3.7.10

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

RUN ipython kernel install --name "python3"

RUN mkdir jupyter_notebooks_outputs

COPY jupyter_notebooks ./jupyter_notebooks

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
