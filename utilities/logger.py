import logging


class Loggen:

    @staticmethod
    def give_logger():
        logging.basicConfig(filename=r'..\Logs\auto.log', level=20)
        logger = logging.getLogger()
        return logger
