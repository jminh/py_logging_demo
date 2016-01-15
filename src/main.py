#!/usr/bin/env python
import logging

from setting import logger
from setting.logger import (ConsoleLogHandler,
                    LogFormatter,
                    set_log_level)


def main():
    set_log_level(logging.INFO)

    console_handler = ConsoleLogHandler()
    logger.addLogHandler(console_handler)

    _log = logging.getLogger('main')


    log_file = 'demo.log'
    try:
        file_handler = logging.FileHandler(log_file, 'w')
        file_handler.setFormatter(LogFormatter())
        logger.addLogHandler(file_handler)
    except:
        print('ERROR: Cannot create file : %s, Permission denied.' % log_file)

    _log.info('Hello')

if __name__ == '__main__':
    main()
