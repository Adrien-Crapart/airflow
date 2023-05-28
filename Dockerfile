FROM apache/airflow:2.6.0
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install markupsafe==2.0.1 \
  && pip install apache-airflow-providers-odbc \
  && pip install pyodbc \
  && pip install apache-airflow-providers-microsoft-mssql \
  && pip install apache-airflow-providers-microsoft-mssql[odbc] \
  && pip install apache-airflow-providers-microsoft-azure \
  && pip install gitpython \
  # && pip install apache-airflow-providers-apache-hdfs \
  # && pip install apache-airflow-providers-apache-hive \
  && pip install apache-airflow-providers-apache-spark \
  && pip install apache-airflow-providers-slack \
  && pip install apache-airflow-providers-http \
  && pip install apache-airflow-providers-postgres \
  && pip install apache-airflow-providers-google \
  && pip install apache-airflow-providers-atlassian-jira \
  && pip install apache-airflow-providers-amazon \
  && pip install apache-airflow-providers-ftp \
  && pip install apache-airflow-providers-mongo \
  && pip install apache-airflow-providers-jenkins \
  && pip install apache-airflow-providers-redis \
  && pip install apache-airflow-providers-samba \
  && pip install apache-airflow-providers-smtp