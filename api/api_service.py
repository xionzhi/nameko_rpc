"""
api service
"""

import time

from flask import Flask, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy


app = Flask(__name__)
RPC_CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


@app.route('/call', methods=['POST'])
def call():
    """
    请求回调
    """
    _url = request.json.get('url')
    _data = request.json.get('data')

    if None in (_url, _data):
        return jsonify({'code': 401, 'msg': 'missing data'}), 401

    with ClusterRpcProxy(RPC_CONFIG) as rpc:
        rpc.call_back.request_back.call_async(_url, _data)
    print(time.time(), _url, _data)
    return jsonify({'code': 200, 'msg': 'request ok', 'data': _data})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
