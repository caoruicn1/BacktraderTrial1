import backtrader as bt

def trying(number):
    result =number+1
    return result

def AddIBFxData(pair="EUR.USD-CASH-IDEALPRO" 
                       ,timeframe=bt.TimeFrame.Minutes, compression=5):
