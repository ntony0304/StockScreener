import csv


import sqlite3
#connect to database
con = None
try: #attempt to create database if not exist
    con = sqlite3.connect(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\new_database.db")
    query = ''' CREATE TABLE stock_data (stock TEXT, open REAL, high REAL, low REAL, last REAL, vol REAL'''
    c = con.cursor() #cursor to execute query
    c.execute(query)
    con.commit()
except:
    pass

finally:
    if con is not None:
        con.close() #close connection to database


#open file method 1
with open(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\210930_A&M.csv", 'r') as file:
    csv_reader = csv.reader(file) #reader from csv library will read all the data and place them to the variable csv_reader (row by row)
    print(csv_reader) #pointer to the data of the csv in the memory
    for row in csv_reader:
        print(row)
        # TODO: put the data to the database

