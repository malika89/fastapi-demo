#!/usr/bin/env sh

export PYTHONPATH=.

# make migrations
alembic revision --autogenerate -m "autogenerate"
# Run migrations
alembic upgrade head

# Create initial data in DB
python -m app.initialiser