from func import *
import pandas as pd
import numpy as np
from datetime import datetime

'''
Save per coin all candle-data per time-point, coin-market prices per coin. 
'''

coin_list = ['BTC', 'ETH', 'SOL', 'ADA', 'MATIC', 'AVAX', 'SAND']
data_list = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
for each in coin_list:
    name = 'CoinPriceData_' + each + '_' + datetime.now().strftime('%d-%m-%Y_%H.%M.%S') + '.csv'
    pd.DataFrame.from_records(np.array(price_list(each))).to_csv(name, index=False, header=data_list)

