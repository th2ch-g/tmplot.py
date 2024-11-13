from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger


def generate_logger(logger_name: str) -> Logger:
    logger = getLogger(logger_name)
    logfmt = "%(levelname)-9s %(asctime)s \
            [%(filename)s.%(funcName)s.%(lineno)d] %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(Formatter(logfmt, datefmt=datefmt))
    logger.addHandler(stream_handler)
    logger.setLevel(DEBUG)

    return logger
