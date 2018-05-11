import datetime as dt
from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.EWrapper import EWrapper
from ib.ext.EClientSocket import EClientSocket

def reply_handler(msg):
    print("Reply:", msg)

conn = Connection.create( host = "127.0.0.1",port=7497,clientId=999)
conn.registerAll(reply_handler)
conn.connect()

reply_handler(conn.isConnected())





'''tickerId	the request's unique identifier.
contract	the contract for which we want to retrieve the data.
endDateTime	request's ending time with format yyyyMMdd HH:mm:ss {TMZ}
durationString	the amount of time for which the data needs to be retrieved:
" S (seconds) - " D (days) " W (weeks) - " M (months) " Y (years)
barSizeSetting	the size of the bar:
1 sec 5 secs 15 secs 30 secs 1 min 2 mins 3 mins 5 mins 15 mins 30 mins
1 hour 1 day
whatToShow	the kind of information being retrieved:
TRADES
MIDPOINT
BID
ASK
BID_ASK
HISTORICAL_VOLATILITY
OPTION_IMPLIED_VOLATILITY
FEE_RATE
REBATE_RATE
useRTH	set to 0 to obtain the data which was also generated outside of the Regular Trading Hours, set to 1 to obtain only the RTH data
formatDate	set to 1 to obtain the bars' time as yyyyMMdd HH:mm:ss, set to 2 to obtain it like system time format in seconds
keepUpToDate	set to True to received continuous updates on most recent bar data. If True, and endDateTime cannot be specified.'''

ticker = 1011
symbol = "EURUSD"
endtime = "20180505 23:59:59 GMT"
goback="1Y"
barsize ="1hour"
datatype ="BID"

conn.reqHistoricalData(ticker,symbol,endtime,goback,barsize,datatype,1,1,False)


