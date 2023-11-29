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

6. start the project
Note: Attention! Use the commands below in the root of the project

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

7. Para acessar o banco de dados postgres
```bash
make postgres
```

8. Accessing the API 
http://127.0.0.1:8000/docs#/

9. CodeChecks: 

check with flake8
```bash
flake8 .
```

check with black
```bash
black --check irrigation_design_system_backend
```

format with black
```bash
black .
```