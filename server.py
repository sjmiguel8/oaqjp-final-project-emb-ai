from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text')
    
    if not text_to_analyze:
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "message": "Invalid text! Please try again!"
        }
        return jsonify(response), 400
    
    result = emotion_detector(text_to_analyze)
    if result.get('dominant_emotion') is None:
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "message": "Invalid text! Please try again."
        }
        return jsonify(response), 400
    
    response = {
        "anger": result.get('anger', 0),
        "disgust": result.get('disgust', 0),
        "fear": result.get('fear', 0),
        "joy": result.get('joy', 0),
        "sadness": result.get('sadness', 0),
        "dominant_emotion": result.get('dominant_emotion', '')
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)