# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:17:02 2020

@author: Andrew
"""


#USE IN CASE TABLES BREAK

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

def delete_user(conn, eagleid):
    """
    Delete a user by eagleid
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM users WHERE eagleid=?'
    cur = conn.cursor()
    cur.execute(sql, (eagleid,))
    conn.commit()
    
def delete_all_users(conn):
    """
    Delete all rows in the users table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM users'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALS_A4.db"

    # create a database connection
    conn = create_connection(database)
 
    # connect pls
    if conn is not None:
        # delete functions
        #delete_user(conn, 1)
        delete_all_users(conn) #do not uncomment unless you intend to delete ALL users
        
        print("Deleted info successfully")
 
        # create tasks table
    else:
        print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
    main()