from app.domains import User
from app.usecases import load_user, create_user, list_user


def test_load_user():
    u = load_user({'id': 'foo', 'name': 'foo'})
    assert u.id == 'foo'
    assert u.name == 'foo'


def test_create_user(mocker):
    repo = mocker.Mock()
    u = create_user('foo', 'foo', repo)
    assert u.id == 'foo'
    assert u.name == 'foo'
    repo.upsert_user.assert_called_once()


def test_list_user(mocker):
    repo = mocker.Mock()
    repo.list_user.return_value = []
    users = list_user(repo)
    assert len(users) == 0

    repo.list_user.return_value = [User(id='foo', name='foo')]
    users = list_user(repo)
    assert len(users) == 1
