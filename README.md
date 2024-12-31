# Mentor Me

A mentor and mentee matching app

## Setup (directly)

*Note: you can just use docker if you only want to get this up and going for testing*

*TODO: populate this section with how to setup required tools: editorconfig, pre-commit, docker, etc*

### Geospatial Prerequisites

Before you start make sure you have the following installed:

https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/geolibs/

We need to install these libraries and tell Django where to find them. This varies by your OS/Platform.

#### Linux

```shell
sudo apt-get install binutils libproj-dev gdal-bin
```

TODO: Show how to insert environment variable in a persistent manner

```shell
export GDAL_LIBRARY_PATH="/path/to/your/gdal/installation"
export GEOS_LIBRARY_PATH="/path/to/your/geos/installation"
```

#### mac

```shell
brew install postgis
```

Then modify your ~/.zprofile file to add these lines

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

Alternatively, it is preferable on Mac to install uv using Brew:

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

    docker compose up --build

### Getting the postgis database up and going (needed for local running)

To run locally you'll need to have docker running on your machine.

then in your terminal, navigate to the folder which containers this file and type the following

    docker compose up db

if you need to wipe your database and start again you can use this command, this will destroy all data.

    docker compose down -v db

*TODO: fill this with howto*

## Deploying

*TODO: fill this with how to*
