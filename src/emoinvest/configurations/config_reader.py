from configparser import ConfigParser


def get_config_reader():
    parser = ConfigParser()
    parser.read('/home/msc/emoinvest/src/emoinvest/configurations/dev.ini')
    return parser
