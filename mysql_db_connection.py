# -*- coding: utf-8 -*-
__author__ = "Shreyash Agarwal"
__copyright__ = "Copyright 2017 Minance. All rights reserved"
__status__ = "Development"

import pymysql


def employee_db(username, password, instance=None):
    """
    This function is used to connect to Minance database employee schema.

    Args:
       name (str):  The username to use.

       password(str): The password to use.

    Optional Args:
       instance (minance_db.INSTANCE): Instance to be used to connect to.

    Returns:
       :class:`pymysql_cursor`, :class:`pymysql_connection` if connected successfuly

       :class:`None`, :class:`None` if error in connecting

    """

    if instance is None:
        database_ip = '104.199.237.201'  # Main DB
    else:
        database_ip = instance

    database_user = username
    database_password = password
    print("da pswddddddddddd", database_password)

    database_selected_db = "TRADING_DB"

    try:
        conn = pymysql.connect(host=database_ip,
                               user=database_user,
                               password=database_password,
                               db=database_selected_db)
        db_cursor = conn.cursor()
        sql_statement = """SELECT DISTINCT(SYMBOL) FROM TRADING_DB.EQUITY_LOG;"""
        db_cursor.execute(sql_statement)
        results = db_cursor.fetchall()

        cleaned_list = []
        for result in results:
            cleaned_list.append(result[0])
        print("clean", cleaned_list)
        return cleaned_list
    except pymysql.err.OperationalError:
        return None, None




employee_db('root', 'aH1LEn9g0hl667tL')



