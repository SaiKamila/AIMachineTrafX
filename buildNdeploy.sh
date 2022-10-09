#!/bin/bash
echo "Building lambda"
rm -rf AIMachineTrafX.zip
zip -r AIMachineTrafX.zip . -x "*.sh" -x "**lambda_layers*"  -x "*.json" -x "**__pycache__*"
aws lambda update-function-code --function-name gatherTrafficWeatherData --zip-file fileb://./AIMachineTrafX.zip