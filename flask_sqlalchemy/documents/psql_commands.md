## SQL-Alchemy Cheatsheet
https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst#set-a-database-url
https://video.udacity-data.com/topher/2019/August/5d5a52af_query-cheat-sheet/query-cheat-sheet.pdf

## Postgres
```buildoutcfg
psql <db_name>
```

- Log in as a particular user
```buildoutcfg
sudo -u <username> -i
```

- Create/Drop db
```buildoutcfg
create <database_name>
dropdb <database_name>
```
- Exit and logout
```buildoutcfg
exit
```

## psql
- Connect
```buildoutcfg
psql <dbname>
```

- List all databases on the server, their owners, and user access levels
```buildoutcfg
\l
```

- Connect to a database named
```buildoutcfg
\c <dbname>
```

- Show database tables
```buildoutcfg
\dt
```

- Describe table schema
```buildoutcfg
\d <tablename>
```

- Quit psql, return to the terminal
```buildoutcfg
\q
```

- Get help, see list of available commands
```buildoutcfg
\?
```