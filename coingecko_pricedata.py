from urllib.request import urlopen
import ssl
import json
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib.dates import MonthLocator, DateFormatter

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = input('Cryptocurrency: ')
html = urlopen('https://api.coingecko.com/api/v3/coins/'+ fh +'/market_chart?vs_currency=usd&days=365', context=ctx).read()
data = html.decode()
js = json.loads(data)
w = js['prices']
x_axis = []
y_axis = []
for i in w:
    x = int(i[0] / 1000)
    y = int(i[1])
    x_axis.append(datetime.utcfromtimestamp(x).strftime('%m-%d-%y %H-%m-%ms'))
    y_axis.append(y)

plt.plot(x_axis,y_axis)
plt.title(fh.title()+ ' Price Chart')
plt.xlabel('Month')
plt.ylabel('Price (USD)')
ax = plt.gca()
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_minor_locator(MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(NullFormatter())
ax.xaxis.set_minor_formatter(DateFormatter('%m'))
plt.gcf().autofmt_xdate()
plt.show()
