- - - - 
### Basic Pre-Requisite Steps ###
    * Register & Get TRAFFIC_API_KEY from https://developer.tomtom.com/route-monitoring/request-access
    * Register & Get WEATHER_API_KEY from https://www.weatherapi.com/api-explorer.aspx
    * Create a DynamoDB Table in AWS
        * Name of Table: XTrafficWeatherData
        * partitionKey: XTraWID
        * sortingKey: locationZip
- - - -

### Application Execution Steps ###
* export TRAFFIC_API_KEY=<provide API Key from TomTom API>
* export WEATHER_API_KEY=<provide API Key from Weather API>
* python-lambda-local -f lambda_handler lambda_function.py event.json
OR
* Update the TRAFFIC_API_KEY and WEATHER_API_KEY in runTest.sh file
* execute: ./runTest.sh

## How to Build and Deploy in AWS Lambda ##
### Pre-Requisites ###
* Please follow the Basic Pre-Requisite All Steps
* Create a Lambda Function in AWS
    1. update Configuration Environment with following Key and Values
    2. TRAFFIC_API_KEY=<provide API Key from TomTom API>
    3. WEATHER_API_KEY=<provide API Key from Weather API>
    4. Ensure AWSIAMRole of Lambda has the full access to DynamoDB e.g. arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
* Verify AWS Cli Installed
    * Follow Steps in https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
* Verify the file cat ~/.aws/credentials with following keys;
    1. aws_access_key_id is active 
    2. aws_secret_access_key is active
* Run buildNDeploy Script
    * ./buildNdeploy.sh
* Execute the Lambda from AWS Console





