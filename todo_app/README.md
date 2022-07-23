## Setup your own repo

- Create migration directory structure
```
pip install flask-migrate
flask db init
```
- Sync models
```
flask db migrate
```
- Upgrate migration
```
flask db upgrade
```

## Run the code
- Create the db manually (see ../flask_sqlalchemy)

- Run the app
```buildoutcfg
python app.py
```