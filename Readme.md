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

5. go to app path

```bash
cd irrigation_design_system_backend
```

6. run app

```bash
uvicorn main:app --reload
```

7. run database

```bash
docker-compose run
```
8. localhost 
http://127.0.0.1:8000/docs#/