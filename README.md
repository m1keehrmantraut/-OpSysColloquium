# OpSysColloquium API

All the algorithms are located at the path ../OpSysColloquium/app/src/algrothims

## Installation and start up

```
git clone
python -m venv {...}/OpSysColloquium/.venv
source .venv/bin/activate
pip -r requirements.txt
```

### Run api local

```
cd app/
PYTHONPATH=app uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

```

Run tests:

```
PYTHONPATH=app/ pytest
```

### Run api in docker

```
docker compose up
```

### Open Swagger

```
http://localhost:8000/docs
```

