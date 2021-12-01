import requests


# controller to get data from api's url
def json_url_beer():
    url = requests.get('https://api.openbrewerydb.org/breweries')
    r = url.json()
    return r
