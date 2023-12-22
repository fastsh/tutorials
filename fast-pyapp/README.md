# FastAPI Service


## Quick start

### Create a service from this bootstrap

* Clone this repository

```sh
git clone git@github.com:Obornes/py-service.git
```

* Remove all .git folders

```sh
( find . -type d -name ".git" && find . -name ".gitignore" && find . -name ".gitmodules" ) | xargs -0 rm -rf
```

* Rename the root folder to your service name
* Move the service folder to your lab folder


### Run the service

```sh
fast app:start
```

### Other project commands help
```sh
fast
```

## Code structure

The structure is based on clean architecture, as per the following article: https://fueled.com/the-cache/posts/backend/clean-architecture-with-fastapi/.
```
├── app
│   ├── api
│   │   ├── dtos
│   │   │   ├── user.py
│   │   ├── libs
│   │   │   ├── auth.py  
│   │   ├── models
│   │   │   ├── user.py
│   │   ├── repositories
│   │   │   ├── memory+UserRepository.py
│   │   ├── routers/v1
│   │   │   ├── default+users.py
│   │   ├── usercases
│   │   │   ├── users.py
│   │   ├── main.py  
│   ├── tests
│       ├── unit
│       ├── integration
│       ├── functional 
│       │   └── collections
├── devops
│       ├── docker-compose.yml 
│       ├── Dockerfile+Dockerfile.test
│       ├── pyproject.toml
│       └── .env
├── Fastfile
├── README.md
└── .gitignore
```

### Add an API

> main -> routers -> usecases -> repositories -> DataBase

* Add a router in api.main or a route in an existing router
* If required create a model and it's validation schema (api.dtos).
* Create a use case 

### Add a Python library
Dependencies are managed with Poetry. 
Declare your library in /devops/pyproject.toml.
Finally remove all containers prefixed with "devops" and start again.

```sh
fast container:cleanup
fast app:start
```

### Configure the service
Environment variables is set in the devops/docker-compose.yml

**Config access in Python**

```python
from decouple import config

config('DATABASE_URL')
```

## Sources
* Architecture:
https://github.com/skhaz/fastapi-clean-architecture
* ORM+Database:
https://coderpad.io/blog/development/sqlalchemy-with-postgresql/
* Data error validation: 
https://fastapi.tiangolo.com/tutorial/schema-extra-example/
* Tests: 
https://docs.pytest.org/en/7.1.x/getting-started.html
