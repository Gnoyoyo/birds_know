import os
from flask import Flask, url_for , Response, json, request, url_for
app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
            'hello' : 'test',

            }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp

@app.route('/', methods = ['GET'])
def api_wellcome():
    return "Hello This is a bird know project"

@app.route('/chat', methods = ['POST'])
def upload_file():
    print(request.files)
    file = request.files['file']
    file.save("./upload/chat.txt")
    return "success"

if __name__ == '__main__':
    app.run()
