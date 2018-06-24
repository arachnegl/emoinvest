from pandas_datareader import data as pdr


def import_single_stock(ticker, date_min, date_max):
    """
    Imports a single ticker symbol for the given time range.
    :param ticker:
    :param date_min:
    :param date_max:
    :return:
    """
    return pdr.get_data_yahoo(ticker, start=date_min, end=date_max)
