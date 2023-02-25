#flask is in virtual env, from bottom right, select venv that you created
from flask import Flask, request, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

@app.route('/api/test', methods = ['GET', 'POST'])
def mytestfunction():
    if request.method == 'GET':
        return jsonify("Kaushika")
    else:
        input_json = request.json
        x = input_json['x']
        # y = input_json['y']
        output = {
            'function' : 'factorial',
            'result' : factorial(x)
        }
        return jsonify(output)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8410)

#batch 4 serial 10

