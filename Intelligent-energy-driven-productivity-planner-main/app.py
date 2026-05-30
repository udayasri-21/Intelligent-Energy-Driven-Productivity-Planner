from flask import Flask, render_template, request, jsonify
from logic import analyze_productivity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/workflow')
def workflow():
    return render_template('workflow.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.json

    result = analyze_productivity(

        float(data['sleep']),
        int(data['stress']),
        float(data['work_hours']),
        int(data['mood'])

    )

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
