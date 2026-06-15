FROM apache/airflow:2.10.5

# Copy requirements
COPY --chown=airflow:root requirements.txt /opt/airflow/requirements.txt

# Install packages
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt