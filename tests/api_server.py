# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6, create time is 20-11-9 下午4:06 GMT+8

import json
from flask import Flask
from flask import request,make_response

app = Flask(__name__)
user_dict = {}

# 创建用户
@app.route('/api/users/<int:uid>', methods=['POST'])
def create_user(uid):
    user = request.get_json()
    if uid not in user_dict:
        result = {
            'success': True,
            'msg': "user created successfully."
        }
        status_code = 201
        user_dict[uid] = user
    else:
        result = {
            'success': False,
            'msg': "user already existed."
        }
        status_code = 500
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


#修改用户
@app.route('/api/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    user = user_dict.get(uid, {})
    if user:
        user = request.get_json()
        success = True
        status_code = 200
    else:
        success = False
        status_code = 404
    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response
#查询客户
@app.route('/api/users/<int:uid>', methods=['GET'])
def search_user(uid):
    user = user_dict.get(uid, {})
    if user:
        success = True
        status_code = 200
    else:
        success = False
        status_code = 404
    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response
#删除用户
@app.route('/api/users/<int:uid>', methods=['DELETE'])
def del_user(uid):
    if uid  in user_dict:
        user_dict.pop(uid)
        result = {
            'success': True,
            'msg': "user deleted successfully."
        }
        status_code = 200
    else:
        result = {
            'success': False,
            'msg': "user inexistence."
        }
        status_code = 500
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response