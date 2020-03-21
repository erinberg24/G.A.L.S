# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:01:05 2020
​
@author: Andrew/Kyle
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
        print(e, "<- hey right here is the error in like 41 i can't figure it out")

def create_user(conn, create_user_sql):
    """ create a user from the create_user statement
    :param conn: Connection object
    :param create_user: a CREATE USER statement
    :return:
    """
    try:
        sql = ''' INSERT INTO user(eagleid,email,password,usertype)
              VALUES(?,?,?,?) '''
        c = conn.cursor()
        c.execute(sql,create_user_sql)
        return c.lastrowid

    except Error as e:
        print(e)


def main():
    #change what you set db equal to
    database = r"C:\Users\Andrew\Documents\GALSDB\sqlite\db\GALSDELTA.db"
    print("POINT ALPHA")

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        eagleid integer,
                                        email text PRIMARY KEY,
                                        password text NOT NULL,
                                        usertype integer,
                                    ); """



    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
        #parameters: eagleid, email, password, usertype
        # usertype 1 = student
        person_1 = (1, 'email1@bc.edu', 'password1', 1)
        # usertype 2 = instructor
        person_2 = (2, 'email2@bc.edu', 'password2', 2)
        # usertype 3 = admin
        person_3 = (3, 'email3@bc.edu', 'password3', 3)
        create_user(conn,person_1)
        create_user(conn,person_2)
        create_user(conn,person_3)
        print("Creation successful")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
