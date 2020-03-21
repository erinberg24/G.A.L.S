# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:27:50 2020

@author: Andrew
"""

import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 

def create_user(conn, users):
    """
    Create a new user into the user table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO users(eagleid,email,password,usertype)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, users)
    return cur.lastrowid
 

def main():
    database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALS_A2.db"
 
    #user creation
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        eagleid integer,
                                        email text PRIMARY KEY,
                                        password text NOT NULL,
                                        usertype integer,
                                    ); """
    
    # create a database connection
    conn = create_connection(database)
    
    with conn:
        
        #make the table
        create_table(conn, sql_create_users_table)
        drop
        print("alpha")
        # userids
        
        # usertype 1 = student
        person_1 = (1, 'tanky@bc.edu', 'password1', 1)
        # usertype 2 = instructor
        person_2 = (2, 'appicels@bc.edu', 'password2', 2)
        # usertype 3 = admin
        person_3 = (3, 'limaw@bc.edu', 'password3', 3)
        person_4 = (4, 'sachdeas@bc.edu', 'epsilon', 1)
        
        # create users
        create_user(conn, person_1)
        create_user(conn, person_2)
        create_user(conn, person_3)
        create_user(conn, person_4)
 
 
if __name__ == '__main__':
    main()