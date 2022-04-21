from flask import Flask, request

app = Flask(__name__)

userList = list()


@app.route('/', methods=['GET'])
def home():
    return "Home"


@app.route('/server', methods=['GET'])
def server():
    return 'Server@v1.0.0.0'


@app.route('/createUser', methods=['POST'])
def createUser():
    name = request.json['name']
    phone = request.json['phone']
    password = request.json['password']

    userList.append(
        {
            'id': len(userList),
            'name': name,
            'phone': phone,
            'password': password
        }
    )

    return {
        'data': 'Successfully createted user!'
    }


@app.route('/users', methods=['GET'])
def getUsers():
    return {
        'data': userList
    }


@app.route('/updateUser/<int:id>', methods=['PUT'])
def updateUser(id):
    name = request.json['name']
    phone = request.json['phone']
    password = request.json['password']

    for i, v in enumerate(userList):
        if v['id'] == id:
            userList.pop(i)

            userList.append({
                'id': id,
                'name': name,
                'phone': phone,
                'password': password
            })

            return {
                'data': 'Successfully updated user'
            }

    return {
        'message': 'user not found'
    }


@app.route('/deleteUser/<int:id>', methods=['DELETE'])
def deleteUser(id):
    for i, v in enumerate(userList):
        if v['id'] == id:
            userList.pop(i)

            return {
                'data': "Successfully deletd user"
            }

    return {
        'message': 'user not found'
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
