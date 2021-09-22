import pandas as pd

class Screener():
    def __init__(self):
        pass
    def filter_by_close_price(self, stock_data, threshold):
        found_data = []
        for item in stock_data:
            if item["close"] > threshold:
                found_data.append(item)
        return found_data
    def create_data_frame(self, stock_data_row):
        df = pd.DataFrame(stock_data_row, columns=["stock", "date","open","high","low","close","volume"])
        return df




class Indicator():

    def __init__(self):
        pass

    def ema(self, price, day):
        return price.ewm(span=day).mean()  # ewm: Exponential Weighted : var(), std(), cov()

    # df['EMA_200'] = ind.ema(df['close'], 200)