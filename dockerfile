FROM python:3.7.10

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../jupyter_notebooks/num_flights_by_country.ipynb ./jupyter_notebooks/
# COPY num_flights_by_country.ipynb ./
