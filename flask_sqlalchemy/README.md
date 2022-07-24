(References from Udacity Full Stack course)
## Run postgres database
- Make sure postgres is installed
```buildoutcfg
$ which postgres

/opt/homebrew/bin/postgres
```
- Start/Stop the server
```buildoutcfg
$ pg_ctl -D /opt/homebrew/var/postgres start
$ pg_ctl -D /opt/homebrew/var/postgres stop
```
## Run the app
```buildoutcfg
python hello_world.py
```
