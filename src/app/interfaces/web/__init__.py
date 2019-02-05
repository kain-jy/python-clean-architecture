from aiohttp.web import Application

from .handlers import routes

app = Application()
app.add_routes(routes)
