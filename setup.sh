#!/usr/bin/env bash

gunicorn liveapi.wsgi -c /code/confs/gunicorn/main.py
