import os
from flask import *
import textconverter
from prediction import predict
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
    file.save("./upload/input.txt")
    textconverter.convert_text("output/input","chat")
    filename = 'chat.csv'
    owner = 'my_line_name'
    output = predict(filename, owner)
    data = {
            'score' :  output

            }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    textconverter.convert_text("output/input","chat")
    filename = 'chat.csv'
    owner = 'my_line_name'
    print(predict(filename, owner))
    app.run()
