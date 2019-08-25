#!/usr/bin/env bash

gunicorn base.wsgi -c /code/confs/gunicorn/main.py
