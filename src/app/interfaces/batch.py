import click
import inject

from .. import usecases

from .redis import UserRedisRepository
from .inmemory import UserInMemoryRepository


def config(redis_url=None):
    def fn(binder):
        if redis_url:
            binder.bind(usecases.UserRepository, UserRedisRepository(redis_url))
        else:
            binder.bind(usecases.UserRepository, UserInMemoryRepository())

    return fn


@click.group()
def cli():
    pass


@cli.command('list-user')
@click.option('--redis-url')
def list_user(redis_url):
    inject.configure(config(redis_url))

    for user in usecases.list_user():
        click.echo("{}:{}".format(user.id, user.name))


if __name__ == '__main__':
    cli()
