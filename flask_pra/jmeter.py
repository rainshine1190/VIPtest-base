from flask import Flask, request, jsonify, make_response
import uuid

app = Flask(__name__)

# 模拟数据库，存储用户信息、商品信息和订单信息
users = {
    'u001': {'userid': 'u001', 'password': 'p001', 'name': 'User One','errorcode':0,'info':{'age':12,'sex':'male'},'books':[1,2,3,4]},
    'u002': {'userid': 'u002', 'password': 'p002', 'name': 'User Two','errorcode':0,'info':{'age':13,'sex':'female'},'books':[5,6,7,8]}
}

products = {
    'product1': {'productid': 'product1', 'name': 'Product One', 'price': 10.99},
    'product2': {'productid': 'product2', 'name': 'Product Two', 'price': 20.99}
}

orders = {
    'u001': [],
    'u002': []
}

order_counter = 1

# 注册接口，JSON入参，返回新用户信息
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    userid = data.get('userid')
    password = data.get('password')
    name = data.get('name')
    age = data.get('age')
    sex = data.get('sex')

    if userid in users:
        return jsonify({'message': 'User already exists', 'errorcode': -1}), 200

    # Creating a new user
    new_user = {
        'userid': userid,
        'password': password,
        'name': name,
        'errorcode': 0,
        'info': {'age': age, 'sex': sex},
        'books': []  # You can customize the initial user data as needed
    }

    users[userid] = new_user

    response = make_response(jsonify(new_user))
    response.set_cookie('userid', userid)  # Set Cookie for the new user
    return response

# 登陆接口，表单入参，返回Cookie信息
@app.route('/login', methods=['POST'])
def login():
    userid = request.form.get('userid')
    password = request.form.get('password')

    if userid in users and users[userid]['password'] == password:
        response = make_response(jsonify(users[userid]))
        response.set_cookie('userid', userid)  # 设置Cookie
        return response
    else:
        return jsonify({'message': 'Invalid credentials','errorcode':-1}), 200

# 获取个人信息接口，从Cookie中获取userid
@app.route('/profile', methods=['GET'])
def profile():
    userid = request.cookies.get('userid')  # 从Cookie中获取userid

    if userid in users:
        return jsonify(users[userid])
    else:
        return jsonify({'message': 'User not found'}), 404

# 查询商品信息接口
@app.route('/get_product', methods=['GET'])
def get_product():
    productid = request.args.get('productid')

    if productid in products:
        return jsonify(products[productid])
    else:
        return jsonify({'message': 'Product not found'}), 404


# 提交订单接口，JSON入参，使用Cookie中的userid
@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    userid = request.cookies.get('userid')  # 从Cookie中获取userid
    productid = data.get('productid')
    order_id = 'd{:03d}'.format(order_counter)  # Generate order ID (e.g., d001)

    if userid in users and productid in products:
        order = {'order_id': order_id, 'productid': productid, 'userid': userid}
        orders[userid].append(order)
        return jsonify({'message': 'Order submitted successfully', 'order_id': order_id})
    else:
        return jsonify({'message': 'User or product not found'}), 404


# 查询订单接口，从Cookie中获取userid
@app.route('/get_orders', methods=['GET'])
def get_orders():
    userid = request.cookies.get('userid')  # 从Cookie中获取userid

    if userid in users:
        return jsonify({'orders': orders[userid]})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
