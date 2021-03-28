#!/bin/bash

echo "Starting Xvfb..."
/usr/bin/Xvfb "$DISPLAY" -ac -screen 0 1024x768x16 +extension RANDR &

echo "Starting gunicorn..."
gunicorn main:app --bind 0.0.0.0:$PORT --timeout 120 --log-level debug
