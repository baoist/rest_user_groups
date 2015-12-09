# Simple JSON API to manage users and groups

## Startup:

- run migrations: `alembic upgrade head`.
- start server: `python rest_user_group/http.py`.

## Usage:
### Users:
- List of all users `GET /users`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET $(docker-machine ip dev)/users`
- Attempt to add a new user `POST /users`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d ' {"first_name": "fname", "last_name": "lname", "userid": "userid"}'  $(docker-machine ip dev)/users`
- Single user `GET /users/<userid>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET $(docker-machine ip dev)/users/<userid>`
- Attempt to update an existing user `PUT /users/<userid>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PUT -d '{"first_name": "fname", "last_name": "lname", "userid": "userid"}' http://127.0.0.1:5000/users/<userid>`
- Attempt to delete an existing user `DELETE /users/<userid>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X DELETE http://127.0.0.1:5000/users/<userid>`

### Groups:
- Single group `GET /groups/<name>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET http://127.0.0.1:5000/groups/<name>`
- Attempt to add a group `POST /groups/<name>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST $(docker-machine ip dev)/groups/<name>`
- Attempt to add a user to a group `PUT /groups/<name>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PUT -d '{"users": ["<userid>"]}' http://127.0.0.1:5000/groups/<name>`
- Empty all users from a group `DELETE /groups/<name>`: `curl -v -H "Accept: application/json" -H "Content-type: application/json" -X DELETE http://127.0.0.1:5000/groups/<name>`
