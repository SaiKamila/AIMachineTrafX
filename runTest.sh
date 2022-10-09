#!/bin/bash
echo "Testing lambda"
export TRAFFIC_API_KEY=
export WEATHER_API_KEY=
python-lambda-local -f lambda_handler lambda_function.py event.json