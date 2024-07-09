import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Leonarda1991!',
        database='mysql'
    )
    if connection.is_connected():
        print('Successfully connected to the database.')
except mysql.connector.Error as err:
    print(f'Error: {err}')
finally:
    if connection.is_connected():
        connection.close()
        print('Database connection closed.')

