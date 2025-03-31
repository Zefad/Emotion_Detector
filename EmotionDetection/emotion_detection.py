import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=myobj, headers=header)
    status_code = response.status_code

    formatted_response = json.loads(response.text)
    if status_code == 200:

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        max_emotion = None
        max_score = None

        for emotion, score in emotions.items():
            if max_score is None or score > max_score:
                max_score = score
                max_emotion = emotion

        emotions['dominant_emotion'] = max_emotion
    elif status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None

    return emotions