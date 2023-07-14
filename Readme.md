## Run Locally

1. create a venv
```bash
python3 -m venv myenv
```
2. Activate the virtual environment:

On macOS/Linux, run:

```bash
source myenv/bin/activate
```
On Windows, run:

```bash
myenv\Scripts\activate
```


3. install requirements.txt
```bash
pip install -r requirements.txt
```

4. go to app path
```bash
cd irrigation_design_system_backend 
```

5. run app
```bash
uvicorn main:app --reload
```
