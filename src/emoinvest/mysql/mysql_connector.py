import PyMySQL
from configurations.

class MySqlConnector:
    """
    This class handles all interactions with the MySQL database that hosts the ticker data
    """

    def insert_or_update_stock_data(self, stock_data_df):
        """

        :param stock_data_df:
        :return:
        """

    def get_mysql_connection(self, db_name):
        con = PyMySQL.connect('localhost', 'testuser', 'test623', 'testdb')
        return con


    def create_stock_database(self, db_name):
        con = self.get_mysql_connection(db_name)