import pymysql

from configurations.config_reader import get_config_reader


class MySqlConnector:
    """
    This class handles all interactions with the MySQL database that hosts the ticker data
    """

    def insert_or_update_stock_data(self, stock_data_df, table_name):
        """
        :param stock_data_df:
        :return:
        """
        con = self.get_mysql_connection('emoinvest')
        try:
            with con.cursor() as cursor:
                for index, row in stock_data_df.iterrows():
                    insert_statement = ("""
                    REPLACE INTO {table_name} (date, ticker_symbol, high, low, open, close, volume, adj_close)
                      Values ('{index}', '{ticker_symbol}', {high}, {low}, {open}, {close}, {volume}, {adj_close})
                    """).format(
                        table_name=table_name,
                        index=index,
                        ticker_symbol=row['ticker_symbol'],
                        high=row['high'],
                        low=row['low'],
                        open=row['open'],
                        close=row['close'],
                        volume=row['volume'],
                        adj_close=row['adj_close']
                    )
                    cursor.execute(insert_statement)
                    con.commit()
        finally:
            con.close()

    @staticmethod
    def get_mysql_connection(db_name):
        configuration_reader = get_config_reader()
        con = pymysql.connect('localhost',
                              configuration_reader.get('settings', 'mysql_user'),
                              configuration_reader.get('settings', 'mysql_pass'),
                              db_name)
        return con

    @staticmethod
    def create_stock_database(db_name):
        configuration_reader = get_config_reader()
        con = pymysql.connect('localhost', configuration_reader.get('settings', 'mysql_user'), configuration_reader.get('settings', 'mysql_pass'))
        try:
            with con.cursor() as cursor:
                sql = ("""
                          CREATE TABLE `emoinvest`.`{db_name}` (
                          `date` DATETIME NOT NULL,
                          `ticker_symbol` VARCHAR(10) NOT NULL,
                          `high` FLOAT NULL,
                          `low` FLOAT NULL,
                          `open` FLOAT NULL,
                          `close` FLOAT NULL,
                          `volume` FLOAT NULL,
                          `adj_close` FLOAT NULL,
                          PRIMARY KEY (`date`, `ticker_symbol`));
                      """).format(
                    db_name=db_name
                )
                cursor.execute(sql)
                con.commit()
        finally:
            con.close()
