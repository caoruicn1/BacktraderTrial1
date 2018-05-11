import datetime as dt

def initialize(context):
    context.sec=superSymbol(secType='FUT', symbol='CL', currency='USD',
                            expiry='201707', exchange = 'NYMEX')

def handle_data(context, data):
    request_data(historyData=[reqHistParam(security=context.sec, 
                            barSize='1 hour',  goBack='100 D',
                            endTime=dt.datetime.now())])
    print data[context.sec].hist['1 hour'].tail()        
    exit()    
