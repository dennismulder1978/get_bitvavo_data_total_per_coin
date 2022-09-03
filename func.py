from Secret import const
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime


bitvavo = Bitvavo({
    'APIKEY': const.api_key,
    'APISECRET': const.api_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def price_list(symbol: str):
    pair = str.upper(symbol) + '-EUR'   # determine pair
    moment = int((datetime.now().timestamp()-435.300)*1000)
    counter = 0
    result = []
    while counter <146:
        try:
            print(symbol + ':' + str(counter) + ':' + str(moment))
            resp = bitvavo.candles(pair, '5m', {'end': moment})
            for i in range(len(resp)):
                resp[i][0] = int(resp[i][0] / 1000)
                result.append(resp[i])
            moment = int((resp[-1][0]-300)*1000)
            counter += 1
        except Exception as e:
            print(e)
            return result

    return result
