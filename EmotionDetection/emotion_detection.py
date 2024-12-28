import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json, headers=headers)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            dominant_emotion = max(emotions, key=emotions.get) if emotions else None
        else:
            anger_score = disgust_score = fear_score = joy_score = sadness_score = 0
            dominant_emotion = None
    else:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = 0
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

if __name__ == "__main__":
    text_to_analyse = input("Enter the text to analyze: ")
    result = emotion_detector(text_to_analyse)
    print(result)