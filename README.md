# Chroma

Randomly choose a colour from a datasource. Provide hexadecimal value and name.

# Requirements
- python >= 3.10
- flask
- rich
- pandas

## for testing
- pytest

# Run tests

From repository root:

```commandline
PYTHONPATH=src pytest tests
```

# To run

- define `DATA_URI` to `data/essential.csv` or run `data/init_db.py` and then set to `data/database.db`
- define `DATA_SOURCE`


## CLI

```commandline
PYTHONPATH=src python -m chroma
```


## REST API

Available endpoints:

- `/` : produces human readable output
- `/colour`: produces json output

To run rest api from repo root:
```commandline
 export DATA_SOURCE=DB_SQLITE 
 export DATA_URI=data/database.db 
 export FLASK_APP=src/chroma/ui/rest/app 
 export FLASK_ENV=development 
 export PYTHONPATH=src
 flask run
```

# Mercurial

https://hg.sr.ht/~pablo_esteban/colour-service