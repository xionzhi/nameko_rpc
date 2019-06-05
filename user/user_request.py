"""
user request
"""

import json
import requests

from datetime import datetime


while True:
    try:
        data = {
            "url": "http://127.0.0.1:5002/back",
            "data": {"date": str(datetime.now())}
        }
        api_url = 'http://127.0.0.1:5001/call'

        resp = requests.post(url=api_url, json=data, timeout=0.5, verify=False, headers={'Content-type': 'application/json'})
        print(resp.text)
    except Exception as e:
        print(e)
