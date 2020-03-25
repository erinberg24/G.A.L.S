# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:33:50 2020

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
 
 
def create_user(conn, user):
    """
    Create a new project into the projects table
    :param conn:
    :param user:
    :return: project id
    """
    sql = ''' INSERT INTO users(eagleid, email, password, usertype)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid


def main():
    database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALS_A4.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        # userinfo
        user1 = (1, "email1@bc.edu", "tester", 1)
        user2 = (2, "email2@bc.edu", "tester", 2)
        user3 = (3, "email3@bc.edu", "tester", 3)
        
        #create users
        create_user(conn, user1)
        create_user(conn, user2)
        create_user(conn, user3)
        print("Data inserted")
 
 
if __name__ == '__main__':
    main()