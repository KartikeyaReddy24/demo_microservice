from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host='database-2.cglvu9svk8cj.us-east-1.rds.amazonaws.com',
        dbname='database-2',
        user='postgres',
        password='123456789'
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f'PostgreSQL version: {db_version}'

