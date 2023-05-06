from flask import Flask, request, jsonify
import requests


API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
headers = {"Authorization": "Bearer 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"}
app = Flask(__name__)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/')
def hello_world():
    return 'welcome to our service'


@app.route('/summarize', methods=['POST'])
def sq():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        text = json["text"]
        finalsummary = ''.join(text)
        output = query({
        "inputs": finalsummary,
        })
        print(output)
        
        return  jsonify(output)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




