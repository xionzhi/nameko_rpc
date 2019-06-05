"""
user service
"""

import time

from flask import Flask, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy


app = Flask(__name__)


@app.route('/back', methods=['POST'])
def call():
    """
    请求回调
    """
    _data = request.json.get('data')

    print(_data)
    return jsonify({'code': 200, 'data': _data})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
