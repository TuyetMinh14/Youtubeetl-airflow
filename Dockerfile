From apache/airflow
COPY requirement.txt /requirement.txt 
RUN pip install --no-cache-dir --user -r /requirement.txt