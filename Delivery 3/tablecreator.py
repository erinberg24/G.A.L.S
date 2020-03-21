# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:01:05 2020

@author: Andrew
"""

import django

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
        return conn
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
 
 
def main():
    database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALSDELTA.db"
    print("POINT ALPHA")
 
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        eagleid integer,
                                        email text PRIMARY KEY,
                                        password text NOT NULL,
                                        usertype text
                                    ); """
 

 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
 
        print("Creation successful")
    else:
        print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
    main()
 
