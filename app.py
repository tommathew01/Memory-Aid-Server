from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to our service'


@app.route('/summarize', methods=['POST'])
def sq():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        txt = json["text"]
        return jsonify({'text': txt})





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




