# Mentor Me

A mentor and mentee matching app

## Setup

*TODO: populate this section with how to setup required tools: editorcondig, pre-commit, docker, etc*

Before you start make sure you have the following installed.

https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/geolibs/

- gdal : `brew install gdal postgis`
- uv: `brew install uv`
- pre-commit: `brew install pre-commit`


To setup your local virtual environement run

    uv venv

To make sure you have all your dependencies installed run this command

    uv sync



## Running and teesting locally

### Getting the postgis database up and going

To run locally you'll need to have docker running on your machine.

then in your teminal, navigate to the folder which containers this file and type the following

    docker-compose up

if you need to wipe your database and start again you can use this command, this will destroy all data.

    docker-compose down -v

*TODO: fill this with howto*

## Deploying

*TODO: fill this with how to*
