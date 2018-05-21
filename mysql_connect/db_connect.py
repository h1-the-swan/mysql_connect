import os
from .MySQLConnect import MySQLConnect

database_settings = {
    'protocol': 'mysql+pymysql',
    'host_name': '127.0.0.1',
    'user_name': os.environ.get('MYSQL_USERNAME'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'encoding': 'utf8mb4',
    'module_path': None,
    'db_name': os.environ.get('MYSQL_DB_NAME')
}

def get_db_connection(db_name=None):
    if database_settings['db_name'] is None:
        if db_name is None:
            raise RuntimeError("db_name not set")
        else:
            database_settings['db_name'] = db_name
    c = MySQLConnect(**database_settings)
    return c

def prepare_base(db):
    # http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html
    from sqlalchemy.ext.automap import automap_base
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    return Base
