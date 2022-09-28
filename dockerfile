FROM python:3.7.10

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN ipython kernel install --name "python3"

RUN mkdir jupyter_notebooks_outputs

COPY jupyter_notebooks ./jupyter_notebooks
