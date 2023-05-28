from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

data = Dataset("/tmp/data.xlsx")


def get_file_to_drive():
    # Chemin vers le fichier JSON des informations d'identification
    credentials_path = '/dags/files/credentials.json'
    # Créer l'objet d'identification
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=['https://www.googleapis.com/auth/drive.readonly'])
    # Créer un client Google Drive
    drive_service = build('drive', 'v3', credentials=credentials)
    # ID du fichier Google Drive que vous souhaitez télécharger
    file_id = '1yo2z6f8k0Pv4nfEoko0QCC991ndGWrsB'
    # Utilisez l'API Google Drive pour récupérer les métadonnées du fichier
    file_metadata = drive_service.files().get(fileId=file_id).execute()
    file_name = file_metadata['name']

    # Téléchargez le fichier localement
    request = drive_service.files().get_media(fileId=file_id)
    file_path = '/data/vers/destination/' + file_name
    with open(file_path, 'wb') as file:
        downloader = googleapiclient.http.MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()


default_args = {
    'start_date': datetime(2023, 5, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG("fast_canal_notification", start_date=datetime(2021, 1, 1),
         schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    downloading_rates = PythonOperator(
        task_id="downloading_rates",
        python_callable=get_file_to_drive
    )

    # @task(outlets=[data])
    # def update_dataset():
    #     with open(data.uri, "a+") as f:
    #         f.write("producer update")

    downloading_rates  # >> update_dataset()
