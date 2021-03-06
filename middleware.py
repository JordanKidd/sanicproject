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
    logging.debug('Server started successfully...')


@mw.listener('before_server_stop')
async def before_server_stop(app, loop):
    logging.debug('Server will be stopping shortly...')


@mw.listener('after_server_stop')
async def after_server_stop(app, loop):
    logging.debug('Server has stopped successfully.')
    database.close()
