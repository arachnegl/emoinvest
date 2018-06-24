from importer



import matplotlib.pyplot as plt

plt.interactive(False)
data["Adj Close"].plot(grid=True)
plt.show()
a = 1

morningstar = pdr.MorningstarDailyReader('GOOGL', start='2018-01-01', end='2018-01-24')