from pandas_datareader import data as pdr


def import_single_stock(ticker_symbol, date_min, date_max):
    """
    Imports a single ticker symbol for the given time range.
    :param ticker:
    :param date_min:
    :param date_max:
    :return:
    """
    stock_data_df = pdr.get_data_yahoo(ticker_symbol, start=date_min, end=date_max)
    stock_data_df['ticker_symbol'] = ticker_symbol
    stock_data_df.columns = ['high', 'low', 'open', 'close', 'volume', 'adj_close', 'ticker_symbol']
    return stock_data_df


def get_single_stock(ticker_symbol, date_min, date_max):
    """
    Returns a single ticker symbol for the given time range from Yahoo finance API.
    :param ticker:
    :param date_min:
    :param date_max:
    :return:
    """
    stock_data_df = pdr.get_data_yahoo(ticker_symbol, start=date_min, end=date_max)
    stock_data_df['ticker_symbol'] = ticker_symbol
    stock_data_df.columns = ['high', 'low', 'open', 'close', 'volume', 'adj_close', 'ticker_symbol']
    return stock_data_df