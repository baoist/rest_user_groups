#!/bin/bash

generate_string()
{
  cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1
}

pause()
{
  read -rsp $'\nPress any key to continue...\n' -n1 key
}

new_userid=$(generate_string)
new_groupid=$(generate_string)

# POST requests
printf "\nPOST\n\n"

printf "Create a user (/users):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X POST -d ' {"first_name": "fname", "last_name": "lname", "userid": "'"$new_userid"'"}' $(docker-machine ip usergroups)/users)"

printf "Create a group (/groups/<groupid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X POST $(docker-machine ip usergroups)/groups/$new_groupid)"

pause

# PUT requests
printf "\nPUT\n\n"

printf "Update a user (/users/<userid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X PUT -d ' {"first_name": "NewFirstName", "last_name": "NewLastName", "userid": "'"$new_userid"'"}' $(docker-machine ip usergroups)/users/$new_userid)"

printf "Attach a user to a group (/groups/<groupid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X PUT -d '{"users": ["'$new_userid'"]}' $(docker-machine ip usergroups)/groups/$new_groupid)"

pause

# GET requests
printf "\nGET\n\n"

printf "Get all users (/users):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" "$(docker-machine ip usergroups)/users")"

printf "Get single user (/users/<userid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" "$(docker-machine ip usergroups)/users/$new_userid")"

printf "Get single group, with associated users (/groups/<groupid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" "$(docker-machine ip usergroups)/groups/$new_groupid")"

pause

# DELETE requests
printf "\nDELETE\n\n"

printf "Detach all users from a group (/groups/<groupid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X DELETE $(docker-machine ip usergroups)/groups/$new_groupid)"

printf "Delete a user (/users/<userid>):\n%s\n" \
  "$(curl -sb -H "Accept: application/json" -H "Content-type: application/json" -X DELETE $(docker-machine ip usergroups)/users/$new_userid)"
