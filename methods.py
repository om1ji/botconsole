import requests
import json

def getMe(token):
    r = requests.get(f'http://api.telegram.org/bot{token}/getMe')
    return r.text