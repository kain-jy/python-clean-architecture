from aiohttp.web import RouteTableDef, Response, json_response

from ... import usecases

routes = RouteTableDef()


@routes.get('/user')
async def list_user(request):
    return json_response({
        'data': [i.dump() for i in usecases.list_user()]
    })


@routes.post('/user')
async def create_user(request):
    data = await request.json()

    user = usecases.create_user(data['id'], data['name'])

    return json_response(user.dump())


@routes.get(r'/user/{user_id}')
async def find_user(request):
    try:
        user = usecases.find_user(request.match_info['user_id'])
    except usecases.UserNotFound:
        return Response(text="", status=404)

    return json_response(user.dump())


@routes.delete(r'/user/{user_id}')
async def delete_user(request):
    try:
        usecases.delete_user(request.match_info['user_id'])
    except usecases.UserNotFound:
        return Response(text="", status=404)

    return Response(text="", status=204)
