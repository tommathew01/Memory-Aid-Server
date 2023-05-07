from flask import Flask, request, jsonify
import requests


API_URL1 = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
headers = {"Authorization": "Bearer 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"}

API_URL2 = "https://api-inference.huggingface.co/models/atharvamundada99/bert-large-question-answering-finetuned-legal"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)


def query1(payload):
    response = requests.post(API_URL1, headers=headers, json=payload)
    return response.json()

def query2(payload):
    response = requests.post(API_URL2, headers=headers, json=payload)
    return response.json()

@app.route('/')
def hello_world():
    return 'welcome to our service'


@app.route('/summarize', methods=['POST'])
def sq():
    content_type = request.headers.get('Content-Type')
    json = request.json
    text = json["text"]
    finalsummary = ''.join(text)
    output = query1({"inputs": finalsummary,})
    print(output[0]["summary_text"].replace(".<n>", ".\n"))
    summary = output[0]["summary_text"].replace(".<n>", ".\n")
    output[0]["summary_text"] = summary
    finaloutput = output[0]
    return finaloutput


@app.route('/search', methods=['POST'])
def pq():
    content_type1 = request.headers.get('Content-Type')
    json1 = request.json
    question = json1["question"]
    summary = json1["summary"]   
    finalquestion = ''.join(question)
    finalsummary = ''.join(summary)
    output1 = query2({
    "inputs": {
        "question": finalquestion,
        "context": finalsummary
        },
    })
    print(output1) 
    return output1



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




