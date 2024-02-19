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

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    show_cursor = db.cursor()

    show_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rowsFetch = show_cursor.fetchall()

    for row in rowsFetch:
        print(row)

    show_cursor.close()
    db.close()
