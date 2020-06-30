#!/bin/sh
# gunicorn run:app --access-logfile - -w 2 --threads 2 -b 0.0.0.0:4000
gunicorn run:app --error-logfile=- --access-logfile=- -w 2 --threads 2 -b 0.0.0.0:4000