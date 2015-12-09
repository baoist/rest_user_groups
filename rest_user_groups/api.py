from models import User, Group
from app import db

def users():
    return User.query.all()

def find_user(userid):
    return User.query.filter(User.userid == userid).first()

def create_user_from_params(params):
    user = User(params.get('first_name'), params.get('last_name'), params.get('userid'))
    db.session.add(user)
    db.session.commit()
    return user

def update_user_from_params(user, params):
    if params.get('first_name'):
        user.first_name = params.get('first_name')
    if params.get('last_name'):
        user.last_name = params.get('last_name')
    if params.get('userid'):
        user.userid = params.get('userid')
    db.session.commit()
    return user

def destroy_user(user):
    db.session.delete(user)
    db.session.commit()
    return user

def find_group(name):
    return Group.query.filter(Group.name == name).first()

def create_group(name):
    group = Group(name)
    db.session.add(group)
    db.session.commit()
    return group

def add_users_to_group(group, users):
    for userid in users:
        user = User.query.filter(User.userid == userid).first()
        group.users.append(user)
    db.session.add(group)
    db.session.commit()
    return group

def empty_users_in_group(group):
    for user in group.users.all():
        group.users.remove(user)

    db.session.add(group)
    db.session.commit()
    return group
