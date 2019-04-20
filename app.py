from flask import Flask, url_for , Response, json
app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
            'hello' : 'test',

            }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp
@app.route('/', methods = ['POST'])
def api_wellcome():
    return "Hello This is a bird know project"
if __name__ == '__main__':
    app.run()
