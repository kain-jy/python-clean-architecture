from app.domains import User


def test_user_init():
    u = User(id='foo', name='foo')
    assert u.id == 'foo'
    assert u.name == 'foo'


def test_user_load():
    u = User.load({'id': 'foo', 'name': 'foo'})
    assert u.id == 'foo'
    assert u.name == 'foo'


def test_user_dump():
    u = User(id='foo', name='foo').dump()
    assert u['id'] == 'foo'
    assert u['name'] == 'foo'
