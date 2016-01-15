import datetime
import logging
import sys

from .logging_without_newline import NewlineStreamHandler

ROOT_LOGGER = logging.getLogger('')
ROOT_LOGGER.setLevel(logging.INFO)


class ConsoleLogHandler(NewlineStreamHandler):
    def __init__(self):
        super(ConsoleLogHandler, self).__init__(sys.stdout)
        self._logger = logging.getLogger('ConsoleLogHandler')
        self.setFormatter(LogFormatter())

    def emit(self, record):
        if record.levelno >= logging.ERROR:
            self._err = True
        super(ConsoleLogHandler, self).emit(record)


class LogFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.INFO:
            fmt = '[{now:%H}:{now:%M}:{now:%S}]  {msg}'
        else:
            fmt = '[{now:%H}:{now:%M}:{now:%S}]  {level}: {msg}'

        return fmt.format(
            now=datetime.datetime.now(),
            level=record.levelname,
            msg=record.msg
        )


_mess_pool = None
def GetLog():
    return _mess_pool


def SetLog(new_logger):
    global _mess_pool
    _mess_pool = new_logger


def set_log_level(level):
    ROOT_LOGGER.setLevel(level)


def addLogHandler(handler):
    ROOT_LOGGER.addHandler(handler)


def removeLogHandler(handler):
    ROOT_LOGGER.removeHandler(handler)
