#!/bin/bash

# Install requirements in case they changed
pip install -r requirements.txt

# Run database upgrades.
# We don't need to wait and sleep for the database to start,
#   as launch order is set in docker-compose.yml
alembic upgrade head