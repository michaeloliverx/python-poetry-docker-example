# Poetry managed Python FastAPI application with Docker multi-stage builds

### This repo serves as a minimal reference on setting up docker multi-stage builds with poetry


### Requirements

- [Docker >= 17.05](https://www.python.org/downloads/release/python-381/)
- [Python >= 3.7](https://www.python.org/downloads/release/python-381/)
- [Poetry](https://github.com/python-poetry/poetry)


---
**NOTE** - Run all commands from the project root


## Local development

---
## Poetry


Create the virtual environment and install dependencies with:

        poetry install

See the [poetry docs](https://python-poetry.org/docs/) for information on how to add/update dependencies.

Run commands inside the virtual environment with:

        poetry run <your_command>

Spawn a shell inside the virtual environment with

        poetry shell

Start a development server locally

        poetry run uvicorn app.main:app --reload --host localhost --port 8000

API will be available at [localhost:8000/](http://localhost:8000/)

Swagger docs at [localhost:8000/docs](http://localhost:8000/docs)

To run testing/linting locally you would execute lint/test in the [scripts directory](/scripts).


---

## Docker


Build images with:
        
        docker build --tag poetry-project --file docker/Dockerfile . 

The Dockerfile uses multi-stage builds to run lint and test stages before building the production stage.  If linting or testing fails the build will fail.

You can stop the build at specific stages with the `--target` option:

        docker build --name poetry-project --file docker/Dockerfile . --target <stage>


For example we wanted to stop at the **test** stage:

        docker build --tag poetry-project --file docker/Dockerfile --target test .

We could then get a shell inside the container with:

        docker run -it poetry-project:latest bash

If you do not specify a target the resulting image will be the last image defined which in our case is the 'production' image.


