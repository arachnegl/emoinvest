import pandas as pd
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from chart_plotting.plot import plot_sector_performance, plot_bbands
from chart_shipping.slack_connector import send_chart
from chart_storage.connector_s3 import save_file_to_s3, build_file_path
from configurations.config_reader import get_config_reader
from dateutil.utils import today

configuration_reader = get_config_reader()


def send_sector_performance():
    sp = SectorPerformances(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')
    data, meta_data = sp.get_sector()
    plot = plot_sector_performance(data)
    file_name = 'sector_performance_' + str(today().strftime('%Y-%m-%d')) + '.png'
    plot.savefig(build_file_path(file_name))
    save_file_to_s3(file_name)
    send_chart('There you  go, here is today´s sector performance', 'Sector Performance', file_name)
    return True


def send_bbands(ticker_symbol: str, days: int) -> True:
    ti = TechIndicators(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')
    data, meta_data = ti.get_bbands(symbol=ticker_symbol, interval='daily', time_period=days)
    ts = TimeSeries(key=configuration_reader.get('settings', 'alpha_vantage_api_key'), output_format='pandas')
    prices, meta_data = ts.get_daily(symbol=ticker_symbol, outputsize='full')
    result = pd.concat([data, prices], axis=1, sort=True)
    file_name = 'BBands_' + str(today().strftime('%Y-%m-%d')) + '_' + ticker_symbol + str(days) + '.png'
    plot = plot_bbands(result, ticker_symbol, days)
    plot.savefig(build_file_path(file_name))
    save_file_to_s3(file_name)
    message = 'There you  go, here are the Bollinger Bands for ' + ticker_symbol
    title = 'Bollinger Bands' + ticker_symbol
    send_chart(message, title, file_name)
    return True
