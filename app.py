"""
Hackathon Project - Real-time Frame Analysis API
------------------------------------------------
This Flask backend powers a real-time computer vision application that:
  1. Receives webcam frames (Base64 encoded) from a frontend.
  2. Detects faces and classifies basic emotions (happy, sad, or neutral).
  3. Returns results as JSON for frontend use.

Core Tech:
  - Flask (API server)
  - OpenCV (image processing)
  - FER (Facial Emotion Recognition)
  - NumPy (matrix operations)
  - Base64 (frontend-backend image transfer)

Intended Use:
  - Hackathon projects
  - Accessibility applications
  - Interactive demos involving emotions detection
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from fer import FER
import os

# --- Initialization ---
app = Flask(__name__)
# Allow requests from frontend (enables cross-origin access)
CORS(app) 

# Initialize the Facial Emotion Recognition model
try:
    # mtcnn=True enables more accurate face detection
    emotion_detector = FER(mtcnn=True)
    print("✅ Emotion detector loaded successfully.")
except Exception as e:
    print(f"⚠️ Error loading emotion detector: {e}")
    emotion_detector = None


# --- Helper Functions ---

def base64_to_image(base64_string):
    """
    Convert a Base64-encoded string from the frontend into an OpenCV image.

    Args:
        base64_string (str): Image encoded as Base64 (with/without header).

    Returns:
        np.ndarray: Decoded OpenCV image in BGR format.
    """
    # Strip the "data:image/jpeg;base64," header if present
    if "," in base64_string:
        base64_string = base64_string.split(',')[1]
    
    # Decode Base64 -> NumPy array -> OpenCV image
    img_data = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return image


def analyze_emotions(image):
    """
    Detect emotions in faces within the image.

    Args:
        image (np.ndarray): OpenCV image in BGR format.

    Returns:
        str: 'happy', 'sad', or 'neutral' (default if unclear).
    """
    if not emotion_detector:
        return "neutral"

    # FER handles RGB conversion internally
    analysis = emotion_detector.detect_emotions(image)
    if not analysis:
        return "neutral"

    # Extract emotions from first detected face
    emotions = analysis[0]['emotions']
    dominant_emotion = max(emotions, key=emotions.get)

    # Restrict to simplified categories
    if dominant_emotion == 'happy':
        return 'happy'
    if dominant_emotion == 'sad':
        return 'sad'
    return 'neutral'


# --- API Endpoint ---

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """
    API endpoint to process an incoming frame.

    Workflow:
      1. Receive JSON with Base64 image.
      2. Decode into OpenCV format.
      3. Run emotion detection.
      4. Return results in JSON.

    Request Body:
      {
        "image": "<base64 string>"
      }

    Response:
      {
        "emotion": "happy" | "sad" | "neutral"
      }
    """
    try:
        data = request.get_json()
        image = base64_to_image(data['image'])

        if image is None:
            return jsonify({'error': 'Invalid image data'}), 400

        # Run AI analysis
        emotion = analyze_emotions(image)

        return jsonify({'emotion': emotion})

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return jsonify({'error': str(e)}), 500


# --- Main Entrypoint ---
if __name__ == "__main__":
    # Hugging Face Spaces automatically sets $PORT
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
