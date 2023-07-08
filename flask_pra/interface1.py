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

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False   # jsonify转变格式的时候不会转变为unicode编码格式，unicode编码格式无法直接看到汉字
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"


# GET接口
@app.route('/get_data', methods=['GET'])
def get_data():
    # 获取GET请求的参数
    username = request.args.get('username')
    # 处理业务逻辑
    if username:
        data = {'message': f'你好，{username}！这是一个GET请求。'}
    else:
        data = {'message': '这是一个GET请求。'}
    return jsonify(data)


# POST表单入参接口
@app.route('/post_form_data', methods=['POST'])
def post_form_data():
    # 获取POST请求的表单数据
    username = request.form.get('username')
    password = request.form.get('password')
    # 处理业务逻辑
    if username and password:
        data = {'message': f'你好，{username}！你的密码是{password}。这是一个带表单数据的POST请求。'}
    else:
        data = {'message': '这是一个带表单数据的POST请求。'}
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
            data = {'message': f'你好，{username}！你的密码是{password}。这是一个带JSON数据的POST请求。'}
        else:
            data = {'message': '这是一个带JSON数据的POST请求。'}
    else:
        data = {'message': '请求中未找到JSON数据。'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
