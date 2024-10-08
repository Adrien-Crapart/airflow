<img src=".github/airflow-picture.png" alt="delivery-service-lambdas" width="100%" height="350" style="border-radius: 15px;padding: 5px;"/>

# Airflow pipelines

[![python_version_img]][python_repos_url][![airflow_version_img]][airflow_url][![repo_version_img]][repo_wiki_url] [![youtube_version_img]][youtube_url][![udemy_version_img]][udemy_url]

<!-- python -->
[python_version_img]: https://img.shields.io/badge/Python-3.9+-00ADD8?style=for-the-badge&lopython=python
[python_repos_url]: https://www.python.org/downloads/

<!-- Airflow -->
[airflow_version_img]: https://img.shields.io/badge/airflow-2.7.0-green?style=for-the-badge&python=none
[airflow_url]: https://airflow.apache.org/docs/

<!-- Repository -->
[repo_version_img]:https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[repo_wiki_url]: https://github.com/Adrien-Crapart/airflow

<!-- Learn space -->
[udemy_version_img]: https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white
[udemy_url]: https://udemy.com/organization/search/?src=ukw&q=airflow
[youtube_version_img]:https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[youtube_url]: https://www.youtube.com/@MarcLamberti

Run your automations from more of 130 logicals operators and schedules every jobs when you want !

## :notebook: Organisation

```bash
airflow-project/
├── dags/
│   ├── data_folder/
│   │    ├── scripts/
│   │    │   └── script.py   
│   │    ├── dag1.py
│   │    ├── changelog.md
│   │    └── schema.drawio
│   ├── .airflowignore
│   └── ...
├── plugins/
│   ├── operators/
│   │   ├── operator1.py
│   │   └── ...
│   ├── sensors/
│   │   ├── sensor1.py
│   │   └── ...
│   └── ...
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── makefile
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

* pyproject.toml : To Help for conflict resolution, please always use requirements.txt for airflow running

* requirements.txt : Manage all depedencies and packages in the airflow containers

## :fire: Local deployment

### For the installation

#### ![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white) With Make (only on wsl, linux or macOS)

First execute `make init` -> `make start`

#### ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) With Docker-compose (all OS)

Initialize airflow in first :
`docker-compose up --build airflow-init postgres`

Then launch the services after build is done :
`docker-compose up --build airflow-webserver airflow-scheduler mail`

### To development

Airflow already has a lot of features and others make it easier to perform tasks.

Develop your constructions in the code and execute your blocks to know the final behavior that your dags will have.

**TIPS:**

* Launch without UI webpage your job with this command :

`airflow tasks test <python-file> <task-name> <date>` 
ex : `airflow tasks test run_zonage_processing execute_ssh_command 2022-01-01`

* Define one job failed or successully executed with the button "Mark state as ..."

* You can also to relaunch on job without relaunch all processing, please use "Clear task" in "Graph" view

#### Drivers or softwares installed on local machine

* Selenium with chromium
* GDAL library ([gdal_url])
* Git ([git_url])

[gdal_url]: (https://gdal.org/)
[git_url]: https://git-scm.com/

#### Libraries installed on local machine

* All pip in requirements.txt, if you add or change please define a specific version to broken anything

TIPS : If you need to install one pip after the installation of docker-compose, enter in airflow scheduler container with `docker exec -it <container-id>` and execute `pip install <library-name>` (to know the name `docker ps`)

### :earth_africa: URL

To access on your local or the production environment, please choose one of this link.
[![apache_airflow_dev]][airflow_local_url] [![mailhog_version_img]][mailhog_url]

[apache_airflow_dev]:https://img.shields.io/badge/Apache%20Airflow%20dev-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white
[airflow_local_url]: http://localhost:8080
[mailhog_version_img]: https://img.shields.io/badge/mailhog-fake%20email-red?style=for-the-badge
[mailhog_url]: http://localhost:8025

## :construction_worker: Authors

* [@Adrien-Crapart](https://www.github.com/Adrien-Crapart)