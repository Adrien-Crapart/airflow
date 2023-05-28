from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# DAG object
from airflow import DAG

# Operators
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator


def get_changed_date():
    response = requests.get(
        'https://cadastre.data.gouv.fr/data/dgfip-pci-vecteur/latest/edigeo/feuilles/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find('pre').text
        element = element.replace(' ', '')
        datetime_object = datetime.strptime(element[8:19], '%d-%b-%Y')

        change_detected = False

        if datetime_object > datetime.strptime('02-Jan-2023', '%d-%b-%Y'):
            # print(f"Change detected! New date at {datetime_object}")
            change_detected = True

        if change_detected:
            return 'task_following_change'
        else:
            return 'task_not_following_change'

    else:
        return 'task_not_following_change'


default_args = {
    'owner': 'Adrien Crapart',
    'description': 'Pipeline de téléchargement et traitement des données du cadastre',
    'start_date': datetime(2023, 5, 20),
    'retries': 0
}


with DAG('cadastre_data_pipeline', default_args=default_args, schedule_interval='@once', catchup=False) as dag:

    choose_model = BranchPythonOperator(
        task_id='choose_model',
        python_callable=get_changed_date,
        do_xcom_push=False
    )

    task_following_change = DummyOperator(
        task_id="task_following_change",
    )

    task_not_following_change = DummyOperator(
        task_id="task_not_following_change",
    )

    choose_model >> [task_following_change, task_not_following_change]
