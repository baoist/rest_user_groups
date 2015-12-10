## Quickstart with Docker

```bash
./run.sh
```

Test existing endpoints.

```bash
./demo.sh
```

Delete the docker machine after you're done.

```bash
docker-machine rm usergroups
```

### Rationalizing

Using docker for ease of spinning up, and to ensure it always runs on Ubuntu.

Given time constraints I decided to omit tests in favor of `demo`ing via curl.
Unfortunately this doesn't catch all of the conditions.
