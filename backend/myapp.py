import flask
from flask import request, jsonify
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Get the question
urlQuest = 'https://api.mentimeter.com/questions/48d75c359ce4'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
resultQuest = requests.get(urlQuest, headers=headers)
resultQuest = json.dumps(resultQuest.json())
quest_data = json.loads(resultQuest)

#Get the results
urlResp = 'https://api.mentimeter.com/questions/48d75c359ce4/result'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
resultResp = requests.get(urlResp, headers=headers)
resultResp = json.dumps(resultResp.json())
resp_data = json.loads(resultResp)

#Format the response
my_dict = {}
my_dict['question'] = quest_data.get('question')
my_dict['results'] = resp_data.get('results')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mentimeter Questions</h1><p>Move to /result to see the results</p>"

@app.route('/results', methods=['GET'])
def api_all():
    return my_dict


app.run(host='0.0.0.0')