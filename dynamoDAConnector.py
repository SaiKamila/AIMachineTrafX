import uuid
import boto3

def store(locationZip, weatherResponse, trafficResponse):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('XTrafficWeatherData')
        trafficResponseFlowSegment = trafficResponse.json()['detailedSegments']
        weatherResponseLocation = weatherResponse.json()['location']
        weatherResponseCurrent = weatherResponse.json()['current']
        id = uuid.uuid1()
        table.put_item(
            Item={
                'XTraWID': str(id),
                'localtime': str(weatherResponseLocation['localtime']),
                'locationName': str(weatherResponseLocation['name']),
                'locationZip': str(locationZip),
                'region': str(weatherResponseLocation['region']),
                'country': str(weatherResponseLocation['country']),
                'latitude': str(weatherResponseLocation['lat']),
                'longitude': str(weatherResponseLocation['lon']),
                'temp_f': str(weatherResponseCurrent['temp_f']),
                'wind_mph': str(weatherResponseCurrent['wind_mph']),
                'wind_degree': str(weatherResponseCurrent['wind_degree']),
                'wind_dir': str(weatherResponseCurrent['wind_dir']),
                'pressure_mb': str(weatherResponseCurrent['pressure_mb']),
                'pressure_in': str(weatherResponseCurrent['pressure_in']),
                'precip_mm': str(weatherResponseCurrent['precip_mm']),
                'humidity': str(weatherResponseCurrent['humidity']),
                'cloud': str(weatherResponseCurrent['cloud']),
                'feelslike_f': str(weatherResponseCurrent['feelslike_f']),
                'vis_miles': str(weatherResponseCurrent['vis_miles']),
                'uv': str(weatherResponseCurrent['uv']),
                'gust_mph': str(weatherResponseCurrent['gust_mph']),
                'currentSpeed': str(trafficResponseFlowSegment[2]['currentSpeed']),
                'relativeSpeed': str(trafficResponseFlowSegment[2]['relativeSpeed']),
                'typicalSpeed': str(trafficResponseFlowSegment[2]['typicalSpeed']),
                'openLrId': str(trafficResponseFlowSegment[2]['openLrId']),
                'averageRouteSpeed': str(3.6 * (float(trafficResponse.json()['routeLength']) / float(trafficResponse.json()['travelTime'])))
            }
        )
        print("The Data inserted Successfully for the XTraWID :" + str(id))
        return id

