import os
from flask import *
import textconverter
from prediction import predict
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['GET'])
def index():
    return send_from_directory("./www", 'index.html')

@app.route('/chat', methods = ['POST'])
def upload_file():
    print("Upload")
    file = request.files['file']
    file.save("input.txt")
    textconverter.convert_text("input","chat")
    filename = 'chat.csv'
    owner = 'Max.'
    output = predict(filename, owner)
    data = {
            'score' :  output

            }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()
