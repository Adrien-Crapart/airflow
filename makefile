.PHONY: init start stop destroy

#First start
init:
	@echo "Init Postgres and Airflow-init containers..."
	@docker-compose build --no-cache
	@docker-compose up -d airflow-init

	@echo "Waiting for Airflow Init service to finish..."
	@while [ $$(docker-compose ps -q airflow-init | wc -l) -ne "0" ]; do sleep 5; done

	@echo "Everything setted up..."
	

#Start without the init part
start:
	@echo "Starting DB containers..."
	@docker-compose up -d postgres

	@echo "Starting Airflow Webserver and Scheduler services..."
	@docker-compose up -d airflow-webserver airflow-scheduler mail

restart:
	@echo "Stop containers..."
	@docker-compose stop

	@echo "Starting DB containers..."
	@docker-compose up -d postgres

	@echo "Starting Airflow Webserver and Scheduler services..."
	@docker-compose up -d airflow-webserver airflow-scheduler mail

#Stop all container
stop:
	@echo "Stop containers..."
	@docker-compose down

#Destroy all docker stack for this project
destroy:
	@echo "Stop and remove containers/images/volumes and networks..."
	@docker-compose down --volumes --rmi all