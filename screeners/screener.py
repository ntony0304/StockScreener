import pandas as pd
import screeners._internal_indicators as ind

# Only alter this for names accross the webapp
SCREENER_NAME = "Break New High Bullish Stock"
CHOICE_A_NAME = "D20"
CHOICE_B_NAME = "D60"
CHOICE_C_NAME = "D250"
            #df, "B" ,          True
def screener(df, choice="B", test=e):
    # If test. Common Variables were not loaded
    #test = True
    if test is True: #if test is true then execute inside
        df['EMA_200'] = ind.ema(df['close'], 200) #indicate
        df['EMA_cond'] = df['close'] > df['EMA_200']
        df['HH_4'] = ind.highest_high(df, 4)

    # Choice A   #df, "B" ,          True
    if choice == "A":
        if not test: # Test = False !Test -> True
            df = df.copy()
            df = df.tail(22)
        df['HH_20'] = ind.highest_high(df, 20)                  #False
        df['main_condition'] = (df['HH_4'] == df['HH_20']) & df['EMA_cond'] #evaluate True or False

    # Choice B   #df, "B" ,          True
    if choice == "B":
        if test: #if test is true
            df['HH_60'] = ind.highest_high(df, 60)
        else:
            df = df.copy()
            df = df.tail(62)
        df['main_condition'] = (df['HH_4'] == df['HH_60']) & df['EMA_cond']

    # Choice C
    if choice == "C":
        if not test:
            df = df.copy()
            df = df.tail(252)
        df['HH_250'] = ind.highest_high(df, 250)
        df['main_condition'] = (df['HH_4'] == df['HH_250'])

    if test: #false
        return df
    return df['main_condition'].iloc[-1]
