# Creating the images and container in docker
up:
	docker-compose up -d

down:
	docker-compose down
	
# Accessing the database in the container
postgres:
	docker exec -it postgres_db bash -c "psql -U postgres"
	
# Initializing the application
start:
	cd ./irrigation_design_system_backend && uvicorn main:app --reload
