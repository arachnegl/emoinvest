
import matplotlib.pyplot as plt

from mysql.mysql_connector import MySqlConnector
from stock_data_importer.stock_import import import_single_stock

ticker = 'DAX'
start='2018-01-01'
end='2018-01-24'

data = import_single_stock(ticker, start, end)

connector = MySqlConnector()
connector.insert_or_update_stock_data(data, 'stocks_daily')
