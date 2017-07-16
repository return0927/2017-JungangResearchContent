import json, requests

def getFeed(Token, until='', url="https://graph.facebook.com/v2.9/818939704832393/feed?since=1499900000&until=1499960302&access_token=EAACEdEose0cBANRIIwH5T1JmIlQHthCAQLhZCZBMWLzqkrDHFqDk2AEfIK4KM3flefY2LrKmFZBxQrIBdAKIvPADHZBh2mZAEDHw7oXtHPC2Tf4Bub3hfubrY9zMPLohYBuGWGuEuJCTcVQ5eZAKyZAdAEczLF97tZBhUiwOXCXoXlD1UQIgrZBoAmDFZA2o0lZBWMZD&limit=5000"):
    #url = url%(Token)

    reqBody = requests.get(url)
    reqBody = json.loads(reqBody.text)
    return reqBody['paging']