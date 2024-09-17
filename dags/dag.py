from airflow.decorators import dag, task
from datetime import datetime, timedelta
import requests

from airflow.io.path import ObjectStoragePath

osp_aws_bucket = ObjectStoragePath('s3://data', conn_id='aws_s3')

@dag(
    start_date=datetime(2022, 1, 1), 
    schedule=None,
    catchup=False
)
def afs():
    
    @task
    def fetch_data(ds=None) -> ObjectStoragePath:
        import pandas as pd
        
        base_url = 'https://jsonplaceholder.typicode.com/comments'
        response = requests.get(base_url)
        df = pd.DataFrame(response.json())
        path = osp_aws_bucket / f'comments_{ds}.json'
        with path.open('wb') as f:
            df.to_parquet(f)
        return path
    
    fetch_data()

afs()