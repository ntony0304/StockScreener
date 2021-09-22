#indicators
import pandas_ta



def ema(price, day):
    return pandas_ta.ema(price, day)  # ewm: Exponential Weighted : var(), std(), cov()

