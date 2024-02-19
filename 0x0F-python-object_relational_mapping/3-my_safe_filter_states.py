#!/usr/bin/python3
"""This code models states
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    show_cursor = db.cursor()

    show_cursor.execute(query, params)
    rowsFetch = show_cursor.fetchall()

    for row in rowsFetch:
        print(row)

    show_cursor.close()
    db.close()
