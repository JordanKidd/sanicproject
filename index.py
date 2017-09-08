from sanic.views import HTTPMethodView
from sanic.response import text


class IndexView(HTTPMethodView):
    """
    This is the class that responds for requests for: /
    """
    decorators = []

    async def get(self, req):
        return text('Hello world!')


class IndexNameView(HTTPMethodView):
    """
    This is the class that responds for requests for: /
    """
    decorators = []

    async def get(self, req, name):
        return text('Hello world and {}'.format(name))
