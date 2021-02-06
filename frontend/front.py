import flask
from flask import request, jsonify
from flask import Response
import requests
import json, ast
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np 
import io

app = flask.Flask(__name__)
app.config["DEBUG"] = True

resultQuest = requests.get("http://python-backend-service.default.svc.cluster.local:5002/results")

data = (resultQuest.json())
providers = []
score = []
for item in data['results']:
        providers.append(item['label'])
        score.append(item['score'])

lp = list(providers)
ls = flat_list = [item for sublist in score for item in sublist]

x = np.arange(len(lp))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, ls, width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Best interactive platform')
ax.set_xticks(x)
ax.set_xticklabels(lp)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
fig.tight_layout()

@app.route('/image')
def plot_png():
    #fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


app.run(host='0.0.0.0')