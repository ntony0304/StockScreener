'''sqlite database'''
import sqlite3
import traceback


class Database():
    def __init__(self, setting):
        self.db_setting = setting # copy all the attributes inside setting and assign to db_setting
        self.connection = sqlite3.connect(self.db_setting.database_file_location)
    def create_stock_table(self):
        #Date	Open	High	Low	Close	Adjusted_close	Volume
        cur = sqlite3.connect(self.db_setting.database_file_location).cursor()
        try:
            cur.execute('''CREATE TABLE stocks (stock TEXT, date DATE,	open REAL,	high REAL,	low REAL,	close REAL, volume INT)''')#create table
            self.connection.commit() #apply the changes to the database
            self.connection.close()
        except: #if the table exist just skip
            pass
