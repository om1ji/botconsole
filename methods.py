import requests
import json

def getMe(token):
    return requests.get(f'http://api.telegram.org/bot{token}/getMe').text