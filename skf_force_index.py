# Python 中的 Force Index 技術指標來衡量買賣壓力 (Technocal Indicator Force Index)
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

def SKF_ForceIndex(symbol,start='1/1/2000',end='8/10/2021',ndays=1):    
    data = web.DataReader(f"{symbol}.TW", data_source='yahoo', start=start, end=end)    
    data = pd.DataFrame(data)

    ForceIndex = pd.Series(data['Close'].diff(ndays) * data['Volume'], name="ForceIndex")
    symbol_ForceIndex = data.join(ForceIndex)    
    ForceIndex = symbol_ForceIndex['ForceIndex']

    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(2,1,1)
    ax.set_xticklabels([])
    plt.plot(data['Close'], lw=1)
    plt.title(f'{symbol}.TW Price Chart')
    plt.ylabel('Close Price')
    plt.grid(True)
    bx=fig.add_subplot(2,1,2)
    plt.plot(ForceIndex,'k',lw=0.75,linestyle='-',label='ForceIndex')
    plt.legend(loc=2,prop={'size':9.5})
    plt.ylabel('ForceIndex Values')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(),rotation=30)
    plt.show()

SKF_ForceIndex(symbol='0050',start='1/1/2001',end='8/10/2021',ndays=1)
#SKF_ForceIndex(symbol='2330',start='1/1/2015',end='8/10/2021',ndays=1)