import logging


class Environment:
    """All config items that are env agnostic"""
    LOGO = ''
    HANDLERS = [logging.StreamHandler(),
                logging.FileHandler('server.log')]


class Dev(Environment):
    """Dev environment"""
    ENVNAME = 'dev'
    DEBUG = True


class Uat(Environment):
    ENVNAME = 'uat'
    DEBUG = False


class Prod(Environment):
    ENVNAME = 'prod'
    DEBUG = False


def get_current_env():
    # TODO: Check current env and return
    return Dev()


def get_current_env_value(key):
    return getattr(get_current_env(), key, None)


def get_logger(name: str):
    # TODO: FIX LOGGING / app.run(log_config=***)
    handler = logging.basicConfig(handlers=get_current_env_value('HANDLERS'))
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
