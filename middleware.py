import logging

from db import database

from sanic import Blueprint

mw = Blueprint('middleware')


@mw.listener('before_server_start')
async def before_server_start(app, loop):
    logging.debug('Server has not started... yet')
    database.connect()


@mw.listener('after_server_start')
async def after_server_start(app, loop):
    logging.debug('Server has started successfully.')
    print('2')


@mw.listener('before_server_stop')
async def before_server_stop(app, loop):
    logging.debug('Server will be stopping shortly...')
    print('3')


@mw.listener('after_server_stop')
async def after_server_stop(app, loop):
    logging.debug('Server has stopped successfully.')
    database.close()
