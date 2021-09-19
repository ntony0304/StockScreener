from scraper import *
from datetime import date, datetime
def main(setting, database):
    database.create_stock_table() #create the stock table

    #scrape data from api
    data = import_data_from_file()
    #send filtered data to database
    for item in data:
        #, stock, date, open, high, low, close, volume):
        data_date = item["date"]
        data_date = datetime.strptime(data_date,"%Y-%m-%d")

        database.insert_data("MCD", data_date,float(item["open"]),float(item["high"]),float(item["low"]),
                                                                                float(item["close"]),int(item["volume"]))
        data_from_database = database.retrieve_rows()
        print(data_from_database)
        test = (database.retrieve_row())
        print(test)
    data_from_database = database.retrieve_rows()
    print(data_from_database)




