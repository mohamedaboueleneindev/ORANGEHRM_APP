import logging

class LogGen:
    def loggen():
        fh = logging.FileHandler('Logs\\automation.log')
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter.datefmt = '%Y-%m-%d %H:%M:%S'  # Specify the desired date/time format
        fh.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(fh)
        return logger