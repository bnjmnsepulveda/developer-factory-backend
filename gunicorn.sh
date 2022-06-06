#!/bin/sh

cd src/ || exit 1;
gunicorn --chdir /app main:app -w 2 --threads 2 -b 127.0.0.1:5000