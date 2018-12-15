import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from chart_plotting.plot import plot_bbands
from chart_shipping.slack_connector import send_chart
from chart_storage.connector_s3 import save_file_to_s3, build_file_path
from configurations.config_reader import get_config_reader

configuration_reader = get_config_reader()

ti = TechIndicators(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')
ts = TimeSeries(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')

ticker_symbol = 'JNJ'
data_plus, meta_data = ti.get_plus_dm(symbol=ticker_symbol)
data_minus, meta_data = ti.get_minus_dm(symbol=ticker_symbol)
prices, meta_data = ts.get_daily(symbol=ticker_symbol, outputsize='full')
result = pd.concat([data_minus, data_plus], axis=1, sort=True)
result = pd.concat([data_plus, prices], axis=1, sort=True)
result = result.tail(300)
result.plot(kind='line')
plt.show()
c = 1



prices, meta_data = ts.get_daily(symbol=ticker_symbol, outputsize='full')

plot = plot_bbands(data, ticker_symbol, 100)


ti = TechIndicators(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')
data, meta_data = ti.get_macd(symbol='AMZN', interval='monthly')

file_name = 'macd.png'
plt.title('MACD APPL stock')
plt.show()
a = build_file_path(file_name)

plt.savefig(a)
save_file_to_s3(file_name)

send_chart('test_message', 'test_title', file_name)
