import json
import uuid
from apiClient import invoke
from dynamoDAConnector import store
import os
import configloader

def lambda_handler(event, context):
    try:
        locationZip = configloader.config['APISection']['locationZip']
        weatherResponse = \
            invoke(configloader.config['APISection']['weatherAPIUrl'] +
                    os.environ['WEATHER_API_KEY'] +
                    "&q=" +
                    locationZip +
                    "&aqi=no")
        trafficResponse = \
            invoke(configloader.config['APISection']['trafficAPIUrl'] +
                   os.environ['TRAFFIC_API_KEY'])
        xTraWID = 'default_values'
        xTraWID = store(locationZip, weatherResponse, trafficResponse)
        print("Data Inserted Successfully")
    except requests.exceptions.HTTPError as error:
        print(error)
    return {
        'statusCode': 200,
        'XTraWID': str(xTraWID),
        'status': 'Success',
    }
