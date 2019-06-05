"""
rpc request
"""

import time
import requests

from nameko.rpc import rpc, RpcProxy



class CallBack(object):
    """
    请求回调
    """
    name = 'call_back'

    @rpc
    def request_back(self, _url: str, _data: dict):
        """
        requests call back url
        """
        print(_url, _data)
        try:
            resp = requests.post(url=_url, json={'data': _data}, timeout=1, verify=False, headers={'Content-type': 'application/json'})
            print(resp.text)
        except Exception as e:
            print(e)
