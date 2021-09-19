import requests

#download data file and import to database before inspection
def import_data_from_file():
    #api key OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX
    url = "https://eodhistoricaldata.com/api/eod/MCD.US?fmt=json&api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d"
    data = requests.get(url).json()
    return data
#access data live
def scrape_data_live():
    pass
