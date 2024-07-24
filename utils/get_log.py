import logging.handlers
from utils.constants import *
import os


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger('InspirationC')
            cls.logger.setLevel(logging.INFO)

            sh = logging.StreamHandler()
            path = LOG_PATH
            if not os.path.exists(path):
                os.makedirs(path)
            filename = path + '/' + 'mylog.log'
            th = logging.handlers.TimedRotatingFileHandler(filename=filename, when="midnight",
                                                           interval=1, encoding="utf-8")


            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] -- %(message)s"
            fm = logging.Formatter(fmt)


            sh.setFormatter(fm)
            th.setFormatter(fm)

            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger




