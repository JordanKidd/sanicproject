from sanic import Sanic

from middleware import mw

from config import (
    get_env,
    get_logger
)

from index import (
    IndexView,
    IndexNameView
)


app = Sanic(name=__name__)
app.config.from_object(get_env())
log = get_logger('root')


def run():
    app.add_route(IndexView.as_view(), '/')
    app.add_route(IndexNameView.as_view(), '/<name>')
    app.blueprint(mw)
    app.run(host='0.0.0.0', port=8080, debug=get_env().DEBUG)


if __name__ == '__main__':
    run()
