# Technocal Indicator Force Index
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt


def ForceIndex(data,ndays):
    ForceIndex = pd.Series(data['Close'].diff(ndays) * data['Volume'], name="ForceIndex")
    data = data.join(ForceIndex)
    return data 

data = web.DataReader("2330.TW", data_source='yahoo', start="1/1/2020", end='8/10/2021')    
data = pd.DataFrame(data)

n=1
symbol_ForceIndex = ForceIndex(data,n)
ForceIndex = symbol_ForceIndex['ForceIndex']

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(2,1,1)
ax.set_xticklabels([])
plt.plot(data['Close'], lw=1)
plt.title('2330TW Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx=fig.add_subplot(2,1,2)
plt.plot(ForceIndex,'k',lw=0.75,linestyle='-',label='ForceIndex')
plt.legend(loc=2,prop={'size':9.5})
plt.ylabel('ForceIndex Values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(),rotation=30)
plt.show()

