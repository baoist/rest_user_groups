## Up and Running

Get started using the API with the following commands:

```bash
docker-machine create -d virtualbox dev
eval "$(docker-machine env dev)"
docker-compose up
```

After this finishes, run the migrations with:

```
docker-compose run web alembic upgrade head
```

## Endpoints

`/users` ["GET", "POST"]
`/users/<name>` ["GET", "PUT", "DELETE"]
`/groups/<name>` ["GET", "POST", "PUT", "DELETE"]

Example
```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET $(docker-machine ip dev)/users
```

# TODO: FIX README

# Project Setup

```
docker-machine create -d virtualbox dev
eval "$(docker-machine env dev)"
```

```
docker-compose up
psql -h $(docker-machine ip dev) -U postgres -c "CREATE DATABASE \"resource-api\";"
docker-compose run web alembic upgrade head
```
