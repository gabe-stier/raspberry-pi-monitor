#################################
# Created on Jul 6, 2020        #
#                               #
# @author: gabezter4            #
#################################
import sqlite3
import hashlib
from datetime import datetime


def post_auth_token(token, name, date):
    success = False
    conn, db = connect()
    if table_exist('auth', db, conn) == False:
        db.execute('''CREATE TABLE auth (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            creation_date TEXT, 
            expired BOOLEAN NOT NULL CHECK (expired IN (0,1)),
            name VARCHAR(50) NOT NULL,
            token VARCHAR(64) NOT NULL UNIQUE
        )
        ''')
        commit(conn)
    db.execute('INSERT INTO auth VALUES(?,?,?,?)', (date, 0, name, token))
    commit(conn)
    conn.close()
    success = True
    return success


def post_vital_sign(sign, value):
    success = False
    conn, db = connect()
    if table_exist("", db, conn) == False:
        db.execute(''' CREATE TABLE vitals (
        request_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        token_id INTERGER NOT NULL,
        temperature INTERGER NOT NULL,
        FOREIGN KEY (token_id) REFERENCES auth (id)
        )
        ''')
    return success


def create_token(name):
    date = datetime.now()
    h = hashlib.sha256()
    h.update(name.encode('utf-8'))
    h.update(str(date).encode('utf-8'))
    hash = h.hexdigest()
    post_auth_token(hash, name, date)
    return hash


def check_token(token):
    conn, db = connect()
    db.execute('SELECT token, expired FROM auth WHERE token=', token)
    row = db.fectchone()
    if(row[0] != token):
        return False
    if(row[1] != 0):
        return False       
    return True


def get_vitals(pi=None):
    success = False
    conn, db = connect()
    if pi == None:
        pass
    
    return success


def table_exist(table, cursor, conn):
    found = False
    cursor.execute('SELECT count(name) FROM sqlite_master WHERE type=\'table\' AND name=?', table)
    if cursor.fetchone()[0] == 1 :
        found = True
    conn.commit()
    return found


def connect():
    database = 'raspberry_pi.db'
    conn = sqlite3.connect(database)
    db = conn.cursor()
    return (conn, db)


def commit(conn):
    conn.commit()


def create_tables():
    sucess = True
    conn, db = connect()
    auth = table_exist('auth', db, conn)  
    pi_info = table_exist('pi_info', db, conn)
    vitals = table_exist('vitals', db, conn)
    
    try:
        if not auth:
            db.execute('''
                CREATE TABLE auth (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    creation_date TEXT, 
                    expired BOOLEAN NOT NULL CHECK (expired IN (0,1)),
                    name VARCHAR(50) NOT NULL,
                    token VARCHAR(64) NOT NULL UNIQUE
                )
            ''')
        
        if not pi_info:
            db.execute('''
                CREATE TABLE pi_info (
                    id INTEGER NOT NULL PRIMARY KEY,
                    hostname VARCHAR(255) NOT NULL,
                    last-beat TEXT NOT NULL,
                    FOREIGN KEY (id) REFERENCES auth (id)
                )
                ''')
        
        if not vitals:
            db.execute('''
                CREATE TABLE vitals (
                    request_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    token_id INTERGER NOT NULL,
                    temperature INTERGER NOT NULL,
                    FOREIGN KEY (token_id) REFERENCES auth (id)
                )
            ''')
        sucess = True
    except Exception:
        sucess = False
    conn.close()
    return sucess
