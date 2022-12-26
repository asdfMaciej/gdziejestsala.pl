#!/bin/bash

# This file is executed after each docker-compose up

# Install requirements in case they changed
pip install -r requirements.txt

# Run database upgrades.
# The database is guaranteed to start, as launch order is set correctly
alembic upgrade head
