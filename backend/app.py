from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_parser import extract_text
from model import ResumeScorer

app = Flask(__name__)
CORS(app)
scorer = ResumeScorer()

@app.route('/api/score', methods=['POST'])
def score_resume():
    jd = request.form.get('job_description')
    file = request.files.get('resume')
    if not jd:
        return jsonify({'error': 'job_description required'}), 400

    if file:
        text = extract_text(file.stream, file.filename)
    else:
        text = request.form.get('resume_text', '')

    if not text:
        return jsonify({'error': 'empty resume text'}), 400

    result = scorer.score(text, jd)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)