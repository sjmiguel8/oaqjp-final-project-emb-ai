from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text')
        
        if not text_to_analyze:
            return jsonify({"error": "Invalid input! Try again."}), 400
        
        result = emotion_detector(text_to_analyze)
        response = {
            "anger": result.get('anger', 0),
            "disgust": result.get('disgust', 0),
            "fear": result.get('fear', 0),
            "joy": result.get('joy', 0),
            "sadness": result.get('sadness', 0),
            "dominant_emotion": result.get('dominant_emotion', '')
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Use POST method to analyze emotions."}), 200

if __name__ == '__main__':
    app.run(debug=True)