#!/bin/bash
echo "******CREATING DOCKER DATABASE******"
export PGUSER=postgres
psql <<- EOSQL
  CREATE DATABASE rest_user_groups;
  GRANT ALL PRIVILEGES ON DATABASE rest_user_groups TO postgres;
EOSQL
echo ""
echo "******DOCKER DATABASE CREATED******"
