import inject
from aiohttp.web import run_app

from . import app
from .config import config


def main():
    inject.configure(config('redis://'))

    run_app(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
