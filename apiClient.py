import requests

def invoke(apiUrl):
    try:
        response = requests.get(apiUrl)
        print('The Api Called Successfully')
    except requests.exceptions.HTTPError as error:
        print(error)
    return response
