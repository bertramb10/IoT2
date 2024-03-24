import sqlite3
from datetime import datetime
from random import randint
from time import sleep

def get_vandtank_data(number_of_rows):
    query = """SELECT * FROM vandtank ORDER BY datetime DESC;"""
    datetimes = []
    temperatures = []
    humidities = []
    conn = None  # Initialize connection variable outside the try block
    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchmany(number_of_rows)
        for row in reversed(rows):
            datetimes.append(row[0])
            temperatures.append(row[1])
            humidities.append(row[2])
        return datetimes, temperatures, humidities
    except sqlite3.Error as sql_e:
        print(f"SQLite error occurred: {sql_e}")
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.close()  # Close the connection if it was opened

get_vandtank_data(10)
