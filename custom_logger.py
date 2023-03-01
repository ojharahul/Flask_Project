import logging
import inspect

class Custom_logger:
    def log(file_name = 'filelog.log',log_level = logging.DEBUG):
        #set class/method from where it is called
        logger_name = inspect.stack()[1][3]

        #Create Logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        logger.handlers = []
        logger.propagate = False

        #Create File hander
        f = logging.FileHandler(file_name)

        #Create Formatter
        #formatter = logging.Formatter('%(asctime)s -- %(levalname)s -- %(name)s -- %(message)s',datefmt= '%m%d%Y %I:%M:%S %p')

        #Add formatter to file handler
        f.setFormatter(logging.Formatter('%(asctime)s -- $(levelname)s -- %(name)s -- %(message)s'))

        logger.addHandler(f)

        return logger


