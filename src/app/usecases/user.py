from abc import ABCMeta, abstractmethod

import inject

from .. import domains


class UserNotFound(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return "User:{} not found".format(self.user_id)


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def list_user(self):
        raise NotImplementedError()

    @abstractmethod
    def find_user(self, user_id):
        raise NotImplementedError()

    @abstractmethod
    def upsert_user(self, user):
        raise NotImplementedError()

    @abstractmethod
    def delete_user(self, user):
        raise NotImplementedError()


def load_user(data):
    return domains.User.load(data)


@inject.autoparams()
def create_user(user_id, name, repository: UserRepository):
    user = domains.User(id=user_id, name=name)

    repository.upsert_user(user)

    return user


@inject.autoparams()
def list_user(repository: UserRepository):
    return repository.list_user()


@inject.autoparams()
def find_user(user_id, repository: UserRepository):
    user = repository.find_user(user_id)
    if not user:
        raise UserNotFound(user_id)

    return user


@inject.autoparams()
def delete_user(user_id, repository: UserRepository):
    user = repository.find_user(user_id)
    if not user:
        raise UserNotFound(user_id)

    repository.delete_user(user)
