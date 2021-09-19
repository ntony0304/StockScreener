from scraper import *
def main(setting, database):
    database.create_stock_table() #create the stock table

    #scrape data from api
    data = import_data_from_file()
    print(data)




