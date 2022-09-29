
"""
============================

============================
"""

from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

#  测试数据
user_info = {"user": 'chenghao', 'pwd': '123456'}

project_data = {"code": "1",
                "results": [
							 {"name": "前程贷1", "id": "1001","desc":"描述1","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "智慧金融2", "id": "1002","desc":"描述2","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "生鲜到家3", "id": "1003","desc":"描述3","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "橙好测试开发4", "id": "1004","desc":"描述4","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "前程贷5", "id": "1005","desc":"描述1","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "智慧金融6", "id": "1006","desc":"描述2","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "生鲜到家7", "id": "1007","desc":"描述3","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "橙好测试开发8", "id": "1008","desc":"描述4","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "前程贷9", "id": "1009","desc":"描述1","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "智慧金融10", "id": "1010","desc":"描述2","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "生鲜到家11", "id": "1011","desc":"描述3","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
							 {"name": "橙好测试开发12", "id": "1012","desc":"描述4","leader":"111","tester":"222","interfaces":"333","testcases":"444","testsuits":"555","publish_app":"666","programmer":"橙好测开"},
						 ],
                "msg": "12个项目",
				"count":12
                }
# 接口数据
interface_data = {
    "1001": {"code": "1",
             "data": [{"name": "前程贷登录1001"},
                      {"name": "前程贷注册1001"}],
             "msg": "2个接口", },

    "1002": {"code": "1",
             "data": [{"name": "智慧-登录1002"},
                      {"name": "智慧-注册1002"},
                      {"name": "智慧-贷款1004"}, ],
             "msg": "3个接口", },

    "1003": {"code": "1",
             "data": [{"name": "生鲜-登录1003"},
                      {"name": "生鲜-注册1003"},
                      {"name": "生鲜下单1003"}, ],
             "msg": "3个接口", },

    "1004": {"code": "1",
             "data": [{"name": "app登录1004"},
                      {"name": "app注册1004"},
                      {"name": "app报名1004"},
                      {"name": "app缴费1004"},
                      ],
             "msg": "4个接口", },
}


# 登录
@app.route('/api/user/login', methods=['post'])
def login():
    """
    接口地址：http://127.0.0.1:5000/api/user/login
    请求方法：post
    参数： {user:账号,pwd:密码}
    参数类型：表单 、json都支持
    返回:该项目的所有接口
    """
    data = request.form or request.json
    # 判断账号，密码是否正确
    if user_info.get('user') == data.get('user') and user_info.get('pwd') == data.get('pwd'):
        return jsonify({'code': "1", "data": None, "msg": "成功"})
    else:
        return jsonify({'code': "0", "data": None, "msg": "密码有误"})



# 获取项目列表
@app.route('/api/projects', methods=['get','post'])
def pro_list1():
    """
    接口地址：http://127.0.0.1:5000/api/projects
    请求方法：get
    参数：无
    返回所有的项目
    :return:
    """
    print(f'目前的project_data:{project_data}')
    if request.method.lower() == 'get':
        return jsonify(project_data)
    elif request.method.lower() == 'post':
        data = request.json
        max_index = project_data['results'][-1]['id']
        data['id'] = int(max_index) + 1
        project_data['results'].append(data)
        return jsonify(project_data)

# 获取项目列表
@app.route('/api/projects/<int:id>/', methods=['delete','put'])
def pro_list2(id):
    """
    接口地址：http://127.0.0.1:5000/api/projects/id
    请求方法：delete,put
    参数：无
    返回所有的项目
    :return:
    """
    global project_data

    if request.method.lower() == 'delete':
        print(f'删除的数据id:{id}')
        Plist = project_data['results']
        for i in Plist.copy():
            print(f'i为{i}')
            if i['id'] == str(id):
                index = Plist.index(i)
                del Plist[index]
                print('----delete')
                break

        project_data['results'] = Plist
        print(f'删除后数据为：{project_data}')
        return jsonify(Plist)

    elif request.method.lower() == 'put':
        data = request.json
        print(f'put接口提交的参数为：{data}')
        Plist = project_data['results']
        for i in Plist.copy():
            print(f'i为{i}')
            if i['id'] == str(id):
                index = Plist.index(i)
                print(f'index为{index}')
                Plist[index] = data
                print('----put')
                break
        return jsonify(Plist)




# 获取接口列表
@app.route('/api/interface', methods=['get'])
def interface():
    """
    接口地址：http://127.0.0.1:5000/api/interface
    请求方法：get
    参数： id(项目的id)
    参数类型：查询字符串
    返回:该项目的所有接口

    """
    inter_id = request.args.get('id')

    if inter_id:
        res_data = interface_data.get(inter_id)
        if res_data:
            return jsonify(res_data)
        else:
            return jsonify({"code": "0", "data": None, "msg": "没有该项目"})
    else:
        return jsonify({"code": "0", "data": None, "msg": "请求参数不能为空"})


if __name__ == '__main__':
    cors = CORS(app)
    app.run(debug=True)

