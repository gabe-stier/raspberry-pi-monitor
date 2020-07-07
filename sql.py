#################################
# Created on Jul 6, 2020        #
#                               #
# @author: gabezter4            #
#################################
import sqlite3
import hashlib
from datetime import datetime


def post_auth_token(token, name):
    success = False
    conn, db = connect()
    if table_exist('auth') == False:
        db.execute('''CREATE TABLE auth (
            id INT NOT NULL PRIMARY KEY AUTOINCREMENT, 
            creation_date TEsXT, 
            expired BOOLEAN NOT NULL CHECK (expired IN (0,1)),
            name VARCHAR(50) NOT NULL,
            token VARCHAR(256) NOT NULL UNIQUE
        ''')
        commit(conn)
    creation_date = datetime.now()
    db.execute('INSERT INTO auth VALUES(?,?,?,?)', (creation_date, 0, name, token))
    commit(conn)
    conn.close()
    success = True
    return success

def post_vital_sign(sign, value):
    success = False
    conn, db = connect()
    
    return success

def create_token():
    success = False
    conn, db = connect()
    
    return success

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

def check_auth_token(token):
    success = False
    
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