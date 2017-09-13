import asyncio
import uvloop
from sanic import Sanic

from middleware import mw

from config import (
    get_current_env_value,
    get_current_env,
    get_logger
)

from index import (
    IndexView,
    IndexNameView
)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(name=__name__)
app.config.from_object(get_current_env())
log = get_logger('root')


def run():
    app.add_route(IndexView.as_view(), '/')
    app.add_route(IndexNameView.as_view(), '/<name>')
    app.blueprint(mw)
    app.run(host='0.0.0.0', port=8080, debug=get_current_env_value('DEBUG'))


if __name__ == '__main__':
    run()
