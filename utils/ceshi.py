import os
import logging
from logging import handlers
import utils.config
from utils.config import LOG_PATH

a = os.path.split(os.path.dirname(os.path.abspath(__file__)))
print(a)
b = os.path.split(os.path.abspath(__file__))
print(b)
c = os.path.dirname(os.path.abspath(__file__))
print(c)
d = os.path.abspath(__file__)
print(d)

class Log():
    def __init__(self,log_name = 'lichutao'):
        self.logger = logging.getLogger(log_name)
        self.log_lever = 'DEBUG'
        self.console_lever = 'WARINING'
        self.log_file_name = 'test.log'
        a = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.pattern = logging.Formatter(a)

    def get_logger(self):

        if not logging.handlers:
            def stream_console(self):
                console = logging.StreamHandler()
                console.setFormatter(self.pattern)
                console.setLevel('INFO')
                return self.logger.addHandler(console)

        else:

            def ratating(self):
                log_handler = logging.handlers.RotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                                   when='D',
                                                                   interval=1,
                                                                   backupCount=self.backup_count,
                                                                   delay=True,
                                                                   encoding='utf-8')
                log_handler.setLevel('DEBUG')
                log_handler.setFormatter(self.pattern)
                return self.logger.addHandler(log_handler)

logger = Log().get_logger()






