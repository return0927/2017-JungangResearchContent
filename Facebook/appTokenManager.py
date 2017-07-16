from setting import settings
import json, requests

class Setting():
    appID = ""
    appSecret = ""
    Token = ""
    pageID = []
    gropuID = []

class Save():
    def getSetting():
        try:
            global Setting
            fileSource = settings.get()
            Setting.appID = fileSource['appID']
            Setting.appSecret = fileSource['appSecret']

            #try:Setting.Token= json.loads(requests.get('https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials'%(Setting.appID, Setting.appSecret)).text)['access_token']
            #finally:Setting.Token = "" if Setting.Token == "" else Setting.Token
            Setting.Token="EAACEdEose0cBANRIIwH5T1JmIlQHthCAQLhZCZBMWLzqkrDHFqDk2AEfIK4KM3flefY2LrKmFZBxQrIBdAKIvPADHZBh2mZAEDHw7oXtHPC2Tf4Bub3hfubrY9zMPLohYBuGWGuEuJCTcVQ5eZAKyZAdAEczLF97tZBhUiwOXCXoXlD1UQIgrZBoAmDFZA2o0lZBWMZD"

            Setting.pageID = fileSource['pageID']
            Setting.gropuID = fileSource['groupID']

            return True
        except Exception as ex:
            return ex


    def saveSetting():
        try:
            global Setting
            legacyTable = {}
            legacyTable['appID'] = Setting.appID
            legacyTable['appSecret'] = Setting.appSecret
            legacyTable['pageID'] = Setting.pageID
            legacyTable['groupID'] = Setting.gropuID
            settings.save(json.dumps(legacyTable, indent=4))

            return True
        except Exception as ex:
            return ex

Save.getSetting()