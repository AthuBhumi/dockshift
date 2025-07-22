#!/bin/bash
source /opt/venv/bin/activate
exec gunicorn --bind 0.0.0.0:$PORT MAIN_APP:app --workers 2 --timeout 60
