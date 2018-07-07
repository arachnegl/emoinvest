
import matplotlib.pyplot as plt

from stock_data_importer.stock_import import import_single_stock

ticker = 'RDSA.AS'
start='1918-01-01'
end='2018-01-24'

data = import_single_stock(ticker, start, end)

data["Adj Close"].plot(grid=True)
plt.show()
a = 1

morningstar = pdr.MorningstarDailyReader('GOOGL', start='2018-01-01', end='2018-01-24')
