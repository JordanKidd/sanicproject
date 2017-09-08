import logging


class Environment:
    """All config items that are env agnostic"""
    LOGO = ''


class Dev(Environment):
    """Dev environment"""
    NAME = 'dev'
    DEBUG = True


class Uat(Environment):
    NAME = 'uat'
    DEBUG = False


class Prod(Environment):
    NAME = 'prod'
    DEBUG = False


def get_env():
    return Dev()


def get_logger(name: str):
    # TODO: FIX LOGGING / app.run(log_config=***)
    handler = logging.StreamHandler()
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
