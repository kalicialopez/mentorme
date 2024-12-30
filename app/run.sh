#!/bin/sh

which python

python --version

pwd

ls -lah

uv pip freeze

uv sync --frozen

uv run manage.py migrate

uv run manage.py runserver 0.0.0.0:8000

echo "DONE."
