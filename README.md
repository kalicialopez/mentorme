# Mentor Me

A mentor and mentee matching app

## Setup (directly)

*Note: you can just use docker if you only want to get this up and going for testing*

*TODO: populate this section with how to setup required tools: editorconfig, pre-commit, docker, etc*

Before you start make sure you have the following installed;

https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/geolibs/
- postgreSQL: mac `brew install postgresql`  
- postgis + gdal: mac `brew install postgis`or linux `sudo apt-get install binutils libproj-dev gdal-bin`
- uv: mac `brew install uv`
- pre-commit: mac `brew install pre-commit`

Modify your ~/.zprofile file to add these lines;

mac
```shell
export GDAL_LIBRARY_PATH="/opt/homebrew/opt/gdal/lib/libgdal.dylib"
export GEOS_LIBRARY_PATH="/opt/homebrew/opt/geos/lib/libgeos_c.dylib"
```

### Project Prerequisites

mentorme requires [uv](https://docs.astral.sh/uv/) for development. The recommended way to install uv is to use
[pipx](https://github.com/pypa/pipx).

```shell
pipx install uv
```

Alternatively, it is possible to install uv using brew:

```shell
brew install uv
```

To setup your local virtual environment run

    uv venv

To make sure you have all your dependencies installed run this command

    uv sync

## Running and testing locally (directly)

    uv run manage.py migrate
    uv run manage.py runserver

## Running and testing locally (docker)

    docker-compose up --build

### Getting the postgis database up and going

To run locally you'll need to have docker running on your machine.

then in your terminal, navigate to the folder which containers this file and type the following

    docker-compose up db

if you need to wipe your database and start again you can use this command, this will destroy all data.

    docker-compose down -v db

*TODO: fill this with howto*

## Deploying

*TODO: fill this with how to*
