from configparser import ConfigParser


def get_config_reader():
    parser = ConfigParser()
    parser.read('./configurations/dev.ini')
    return parser
