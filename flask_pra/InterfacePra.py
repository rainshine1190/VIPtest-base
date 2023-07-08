"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
导包
    1-
    2-
    3-

"""
from flask import Flask, request, jsonify
from flask import make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False   # jsonify转变格式的时候不会转变为unicode编码格式，unicode编码格式无法直接看到汉字
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

JSON_RESPONSE_CONTENT_TYPE = 'application/json;charset=UTF-8'

def _custom_response(json_string):

    response = make_response(jsonify(json_string))

    response.headers['Content-Type'] = JSON_RESPONSE_CONTENT_TYPE

    return response

# GET接口
@app.route('/get_data', methods=['GET'])
def get_data():
    """
    该接口请求路径为：/get_data
    可选参数：username
    :return:
    """
    # 获取GET请求的参数
    username = request.args.get('username')
    # 处理业务逻辑
    if username:
        data = {
            'topic': '这是橙好的get调试接口',
            'message': f'Hello, {username}! This is a GET request.'
        }
    else:
        data = {
            'topic': '这是橙好的get调试接口',
            'message': 'This is a GET request.'
        }
    return _custom_response(data)


# POST表单入参接口
@app.route('/post_form_data', methods=['POST'])
def post_form_data():
    # 获取POST请求的表单数据
    username = request.form.get('username')
    password = request.form.get('password')
    # 处理业务逻辑
    if username and password:
        data = {
            'topic': '这是橙好的post-表单调试接口',
            'message': f'Hello, {username}! Your password is {password}. This is a POST request with form data.'
        }
    else:
        data = {
            'topic': '这是橙好的post-表单调试接口',
            'message': 'This is a POST request with form data.'
        }
    return jsonify(data)


# POST JSON入参接口
@app.route('/post_json_data', methods=['POST'])
def post_json_data():
    # 获取POST请求的JSON数据
    data_json = request.get_json()
    if data_json:
        username = data_json.get('username')
        password = data_json.get('password')
        # 处理业务逻辑
        if username and password:
            data = {
                'topic': '这是橙好的post-json入参调试接口',
                'message': f'Hello, {username}! Your password is {password}. This is a POST request with JSON data.'
            }
        else:
            data = {
                'topic': '这是橙好的post-json入参调试接口',
                'message': 'This is a POST request with JSON data.'
            }
    else:
        data = {
            'topic': '这是橙好的post-json入参调试接口',
            'message': 'No JSON data found in the request.'
        }
    return jsonify(data)


# PUT接口
@app.route('/put_data/<int:id>', methods=['PUT'])
def put_data(id):
    # 获取PUT请求的JSON数据
    data_json = request.get_json()
    if data_json:
        # 处理业务逻辑
        # 假设更新数据的逻辑为将id和更新的数据合并
        data = {**data_json, 'id': id}
        response = {'message': f'Data with id {id} has been updated.', 'data': data}
    else:
        response = {'message': 'No JSON data found in the request.'}
    return jsonify(response)


# DELETE接口
@app.route('/delete_data/<int:id>', methods=['DELETE'])
def delete_data(id):
    # 处理业务逻辑
    # 假设删除数据的逻辑为根据id删除数据
    response = {'message': f'Data with id {id} has been deleted.'}
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)
