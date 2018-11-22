import matplotlib.pyplot as plt


def plot_bbands(data, ticker, days):
    data = data.tail(days)
    data.plot()

    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(111)

    x_axis = data.index.get_level_values(0)
    ax.fill_between(x_axis, data['Real Upper Band'], data['Real Lower Band'], color='grey')
    ax.plot(x_axis, data['Real Middle Band'], color='blue', lw=2)
    ax.plot(x_axis, data['4. close'], color='black', lw=2)

    # Set Title & Show the Image
    ax.set_title(str(days) + ' Day Bollinger Band For ' + ticker)
    ax.set_xlabel('Date (Year/Month)')
    ax.set_ylabel('Price(USD)')
    ax.legend()
    return plt


def plot_macd(data):

    return True


def plot_sector_performance(data):
    data['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per Sector')
    plt.tight_layout()
    plt.grid()
    return plt
