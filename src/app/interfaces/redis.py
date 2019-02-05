import json

import redis

from .. import usecases


class UserRedisRepository(usecases.UserRepository):
    def __init__(self, url):
        self.client = redis.from_url(url, decode_responses=True)

    def list_user(self):
        ret = []
        for k in self.client.keys('user:*'):
            user = usecases.load_user(json.loads(self.client.get(k)))
            ret.append(user)
        return ret

    def find_user(self, user_id):
        payload = self.client.get('user:{}'.format(user_id))
        if not payload:
            return None
        return usecases.load_user(json.loads(payload))

    def upsert_user(self, user):
        self.client.set("user:{}".format(user.id), json.dumps(user.dump()))

    def delete_user(self, user):
        self.client.delete("user:{}".format(user.id))
