#!/bin/sh

cd src/ || exit 1;
gunicorn --chdir /app main:app -w 2 --threads 2 -b 0.0.0.0:8080
