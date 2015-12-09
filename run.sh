#!/bin/bash
cp .env.example .env
docker-machine create -d virtualbox usergroups
eval "$(docker-machine env usergroups)"
docker-compose up
