from app import app

# Press the green button in the gutter to run the script.
import general_functions
from database import Database
import settings
if __name__ == '__main__':
    '''initialize settings'''
    #setting = settings.Setting(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\setting.conf")

    setting = settings.Setting() #initialize the settings
    my_database = Database(setting)
    general_functions.main(setting,my_database)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
