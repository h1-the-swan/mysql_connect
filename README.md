# db_connect_mag

Utilities to connect to local MySQL databases.

Before importing, environment variables must be set:

```
MYSQL_USERNAME="myusername"
MYSQL_PASSWORD="mypassword"
MYSQL_DB_NAME="dbname" (this one is optional. if it is set, it will be used to choose the database)
```

One way to set these is to use the `python-dotenv` library (`pip install python-dotenv`) and load the variables from a `.env` file (which you do not commit to version control):

```
from dotenv import load_dotenv
load_dotenv('.env')
```
