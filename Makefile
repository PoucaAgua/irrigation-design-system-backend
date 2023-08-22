up:
	docker-compose up -d
	
postgres:
	docker exec -it postgres_db bash -c "psql -U postgres"
	