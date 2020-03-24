# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:31:55 2020

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
        #creates database in memory
        conn = sqlite3.connect(':memory:')
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
    #database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALS_A4.db"
 
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        eagleid integer PRIMARY KEY,
                                        email text NOT NULL,
                                        password text NOT NULL,
                                        usertype integer NOT NULL
                                    ); """
 

    # create a database connection
    conn = create_connection()
 
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
        
        print("Table created successfully")
 
        # create tasks table
    else:
        print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
    main()
