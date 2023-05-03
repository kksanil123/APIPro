import configparser

config = configparser.RawConfigParser()
config.read(r'./configurations/config.ini')

prod_service_url = config.get('Domain_Info', 'prod_domain')