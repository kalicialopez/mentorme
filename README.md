# Mentor Me

A mentor and mentee matching app

## Setup

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

To setup your local virtual environment run

    uv venv

To make sure you have all your dependencies installed run this command

    uv sync

## Running and teesting locally

    uv run manage.py migrate
    uv run manage.py runserver

### Getting the postgis database up and going

To run locally you'll need to have docker running on your machine.

then in your terminal, navigate to the folder which containers this file and type the following

    docker-compose up

if you need to wipe your database and start again you can use this command, this will destroy all data.

    docker-compose down -v

*TODO: fill this with howto*

## Deploying

*TODO: fill this with how to*
