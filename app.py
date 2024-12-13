from flask import Flask, request, jsonify
from url_analyzer import analyze_url_features

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_url():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    analysis_result = analyze_url_features(url)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
