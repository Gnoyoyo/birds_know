import os
from flask import *
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
def index():
    return send_from_directory("./www", 'index.html')


@app.route('/chat', methods = ['POST'])
def upload_file():
    file = request.files['file']
    file.save("./upload/chat.txt")
    return "success"

if __name__ == '__main__':
    app.run()
