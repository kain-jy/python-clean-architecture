from ... import usecases

from ..redis import UserRedisRepository
from ..inmemory import UserInMemoryRepository


def config(redis_url=None):
    def fn(binder):
        if redis_url:
            binder.bind(usecases.UserRepository, UserRedisRepository(redis_url))
        else:
            binder.bind(usecases.UserRepository, UserInMemoryRepository())

    return fn
