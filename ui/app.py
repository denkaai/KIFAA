import sys
import time
import numpy as np
from flask import Flask, render_template, jsonify, send_file

sys.path.insert(0, '/home/denkaai/KIFAA/engine1_shield')
sys.path.insert(0, '/home/denkaai/KIFAA/engine2_trace')

app = Flask(__name__,
    template_folder='/home/denkaai/KIFAA/ui/templates',
    static_folder='/home/denkaai/KIFAA/ui/static')

def convert(obj):
    if isinstance(obj, dict):
        return {k: convert(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert(i) for i in obj]
    elif hasattr(obj, 'item'):
        return obj.item()
    return obj

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scan')
def scan():
    from shield import run_shield
    from trace import run_trace
    start = time.time()
    threats = run_shield()
    results = run_trace()
    elapsed = round(time.time() - start, 2)
    return jsonify(convert({'threats': threats, 'results': results, 'time': elapsed}))

@app.route('/graph')
def graph():
    return send_file('/home/denkaai/KIFAA/reports/fraud_network.png', mimetype='image/png')

@app.route('/report')
def report():
    return send_file('/home/denkaai/KIFAA/reports/KIFAA_CASE_REPORT.txt', as_attachment=True)

if __name__ == '__main__':
    print("KIFAA Web Platform starting...")
    print("Open browser: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
