# Emotion Detection Web Application

A web application that analyzes text to detect emotions using IBM Watson's Natural Language Processing service. The application provides a user-friendly interface to input text and displays the detected emotions along with their intensity scores.

## Features

- Real-time emotion detection from text input
- Detects five primary emotions:
  - Joy
  - Anger
  - Disgust
  - Fear
  - Sadness
- Provides emotion intensity scores
- Identifies the dominant emotion
- Clean and intuitive web interface

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Zefad/Emotion_Detector.git
cd Emotion_Detector
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter the text you want to analyze in the input field
4. Click "Run Sentiment Analysis" to get the emotion detection results

## Project Structure

```
final_project/
├── EmotionDetection/
│   └── emotion_detection.py    # Core emotion detection logic
├── static/
│   └── mywebscript.js         # Frontend JavaScript
├── templates/
│   └── index.html            # Main web interface
├── server.py                 # Flask server implementation
├── test_emotion_detection.py # Unit tests
└── requirements.txt          # Project dependencies
```

## API Endpoints

- `GET /`: Main page
- `GET /emotionDetector`: Emotion detection endpoint
  - Query parameter: `textToAnalyze` (text to analyze)

## Dependencies

- Flask 3.0.0
- Requests 2.31.0

## Note

This application requires access to the IBM Watson NLP service. You'll need to:
1. Set up an IBM Watson account
2. Configure the service credentials
3. Update the service URL in `emotion_detection.py` if needed


