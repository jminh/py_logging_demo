import logging


class NewlineStreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(NewlineStreamHandler, self).__init__(stream)
        self.__last_newline = True

    def emit(self, record, newline=True):
        msg = self.format(record)
        newline = getattr(record, 'newline', True)
        if newline:
            if (not self.__last_newline):
                self.stream.write('\n')
            self.stream.write('%s\n' % msg)
        else:
            self.stream.write('%s\r' % msg)
            self.stream.flush()
        self.__last_newline = newline


def get_no_newline_logger(logger):
    assert isinstance(logger, logging.Logger)
    return logging.LoggerAdapter(logger, {'newline': False})
