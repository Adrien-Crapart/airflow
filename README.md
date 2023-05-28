# Automations

Run automations Dags on schedulers and trigger all scripts or dependences




## Organisation

- Dags folder
    - Dags run and schedulers
    - Scripts
    - Data files

- Configuration
    - `Change settings for dags runs`

- requirements
    - `Add news libraries for scripts`
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

PostgreSQL variables

`AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`

`AIRFLOW__CORE__SQL_ALCHEMY_CONN`

`AIRFLOW__CELERY__RESULT_BACKEND`

Create User Admin

`_AIRFLOW_WWW_USER_USERNAME`

`_AIRFLOW_WWW_USER_PASSWORD`
## Deployment

To build all images on Docker with separates volumes

```bash
  docker-compose up -d --build
```


## Authors

- [@adrien.crapart](https://www.github.com/Adrien-Crapart)
