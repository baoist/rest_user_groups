from flask import Flask, jsonify, request, Response
from models import db
import api

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

@app.route('/users', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        users = api.users()
        return jsonify(users=[row._asdict() for row in users])
    else:
        try:
            user = api.create_user_from_params(request.get_json())
            return jsonify(user=user._asdict())
        except:
            return Response(response='Unable to create user.',
                            status=400,
                            mimetype="application/json")

@app.route('/users/<path:userid>', methods=['GET'])
def get_user(userid):
    user = api.find_user(userid)

    if user is None:
        return Response(response='User not found.', status=404, mimetype="application/json")

    if request.method == 'GET':
        return jsonify(user=user._asdict())

@app.route('/users/<path:userid>', methods=['PUT'])
def update_user(userid):
    user = api.find_user(userid)

    try:
        user = api.update_user_from_params(user, request.get_json())

        return jsonify(user=user._asdict())
    except:
        return Response(response='Unable to update user.',
                        status=400,
                        mimetype="application/json")

@app.route('/users/<path:userid>', methods=['DELETE'])
def delete_user(userid):
    user = api.find_user(userid)

    try:
        api.destroy_user(user)
        return Response(response='Successfully deleted user.',
                        status=200,
                        mimetype="application/json")
    except:
        return Response(response='Unable to delete user.',
                        status=400,
                        mimetype="application/json")

@app.route('/groups/<path:name>', methods=['GET'])
def get_group(name):
    group = api.find_group(name)

    if group is None:
        return Response(response='Group not found.', status=404, mimetype="application/json")

    if not group.users.all():
        return Response(response='Group has no associated users.', status=404, mimetype="application/json")

    return jsonify(group=group._asdict(),
                   users=[row._asdict() for row in group.users])

@app.route('/groups/<path:name>', methods=['POST'])
def create_group(name):
    group = api.find_group(name)

    if group is not None:
        return Response(response='Group already exists.', status=404, mimetype="application/json")
    else:
        group = api.create_group(name)
        return jsonify(group=group._asdict())

@app.route('/groups/<path:name>', methods=['PUT'])
def update_group(name):
    group = api.find_group(name)

    if group is None:
        return Response(response='Group not found.', status=404, mimetype="application/json")

    params = request.get_json()
    users = params.get('users')
    if users:
        group = api.add_users_to_group(group, users)
        return jsonify(group=group._asdict(),
                       users=[row._asdict() for row in group.users])
    else:
        return Response(response='No users provided.', status=404, mimetype="application/json")

@app.route('/groups/<path:name>', methods=['DELETE'])
def delete_group(name):
    group = api.find_group(name)

    if group is None:
        return Response(response='Group not found.', status=404, mimetype="application/json")

    if not group.users.all():
        return Response(response='Group has no associated users.', status=404, mimetype="application/json")

    group = api.empty_users_in_group(group)
    return Response(response='All users removed from "%s".' % group.name, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run()
