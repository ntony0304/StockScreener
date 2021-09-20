from scraper import *
from datetime import date, datetime
import screener
def main(setting, database):
    database.create_stock_table() #create the stock table

    #scrape data from api
    # data = import_data_from_file()
    #send filtered data to database
    # for item in data:
    #     #, stock, date, open, high, low, close, volume):
    #     data_date = item["date"]
    #     data_date = datetime.strptime(data_date,"%Y-%m-%d")
    #
    #     database.insert_data("MCD", data_date,float(item["open"]),float(item["high"]),float(item["low"]),
    #                                                                             float(item["close"]),int(item["volume"]))
    #     data_from_database = database.retrieve_rows()
    #     print(data_from_database)
    #     test = (database.retrieve_row())
    #     print(test)
    #data_from_database = database.retrieve_some_rows(100)


    #filter the rows using a predefine threshold
    # filtered_data = my_screener.filter_by_close_price(data_from_database, 53.5000)
    # for item in filtered_data:
    #     print (item)
    #

    row_data = database.retrieve_rows(100)

    my_screener = screener.Screener()  # Screener Object

    df = my_screener.create_data_frame(row_data)

    #print(df)
    df['EMA5'] = my_screener.EMA_indicator(df['close'], 5)
    df['EMA100'] = my_screener.EMA_indicator(df["close"],100)
    print(df)





'''
Explaination for 
def screener(df, choice="A", test=False):
    # If test. Common Variables were not loaded
    if test:
        df['EMA_200'] = ind.ema(df['close'], 200)
        df['EMA_cond'] = df['close'] > df['EMA_200']
        df['HH_4'] = ind.highest_high(df, 4)

'''
#in the program they have a class that will have indicator function
#to use the class they will create the object, here the object name is ind
    ind = screener.Indicator()  #construct ind object

    df['EMA_200'] = ind.ema(df['close'], 200) #add indicator to dataframe by calling ema method from object ind
                        #the input is the close price and the day






