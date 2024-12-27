from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detection', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text')
    
    if not text_to_analyze:
        return jsonify({"error": "Invalid input! Try again."}), 400
    
    result = emotion_detector(text_to_analyze)
    
    if result['label'] is None:
        return jsonify({"error": "Invalid input! Try again."}), 400
    else:
        return jsonify({
            "message": "The given text has been identified as {} with a score of {}.".format(result['label'], result['score'])
        })

if __name__ == '__main__':
    app.run(debug=True)