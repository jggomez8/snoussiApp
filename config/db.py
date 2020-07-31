import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/warrior.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covid',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}


# mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# pyodbc

SQLSERVER = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'db',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 10.0',
        },
    },
}

HEROKU = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dehl1opbffsq44',
        'USER': 'nyfiyhqywkyxki',
        'PASSWORD': '426bf2651dbf51b742411d58603e4445832492c67c578521fe3fbed220d9e160',
        'HOST': 'ec2-52-44-55-63.compute-1.amazonaws.com',
        'PORT': '5432',
     }
 }
