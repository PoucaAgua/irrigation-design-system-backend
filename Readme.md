## Run Locally

1. install python version

```bash
sudo apt install python3.8
```

2. create a venv

```bash
python3.8 -m venv .venv
```

3. Activate the virtual environment:

On macOS/Linux, run:

```bash
source .venv/bin/activate
```

On Windows, run:

```bash
.venv\Scripts\activate
```

4. install requirements.txt

```bash
pip install -r requirements.txt
```

5. Environment variables
- Copy the .env-dev file
- Save as .env inside irrigation_design_system_backend

## Initializing the application
6. Attention! Use the commands below in the root of the project

To create the docker images and containers
```bash
make up
```

To run the application
```bash
make start
``` 

To remove the containers
```bash
make down
``` 

## Accessing the database
7. Para acessar o banco de dados postgres
```bash
make postgres
```

## Accessing the API
8. localhost 
http://127.0.0.1:8000/docs#/