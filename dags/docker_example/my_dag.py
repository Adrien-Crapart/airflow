from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'description': 'DAG to run docker container',
    'depend_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

@dag('docker_example', default_args=default_args, schedule_interval='@daily', catchup=False)

def docker_dag():
    
    @task()
    def t1():
        pass
    
    t2 = DockerOperator(
        task_id='t2',
        image='python:3.8-slim-buster',
        container_name='docker_operator_t2',
        api_version='auto',
        auto_remove=True,
        command='echo "command running in the docker container"',
        docker_url="TCP://docker-socket-proxy:2375",
        network_mode="bridge"
    )

    t1() >> t2
    
dag = docker_dag()