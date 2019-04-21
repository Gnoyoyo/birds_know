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
    #return render_template("www/indexTest.html")

@app.route('/assets/js/<path:path>')
def send_js(path):
    return send_from_directory('./www/assets/js/', path)

@app.route('/assets/css/<path:path>')
def send_css(path):
    return send_from_directory('./www/assets/css/', path)

@app.route('/assets/image/<path:path>')
def send_image(path):
    return send_from_directory('./www/assets/image/', path)

@app.route('/assets/font/<path:path>')
def send_font(path):
    return send_from_directory('./www/assets/font/', path)


@app.route('/chat', methods = ['POST'])
def upload_file():
    print("Upload")
    file = request.files['file']
    file.save("input.txt")
    textconverter.convert_text("input","chat")
    filename = 'chat.csv'
    owner = 'Max.'
    print("Before")
    output = predict(filename, owner)
    data = {
            'score' :  output

            }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()
