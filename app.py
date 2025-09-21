from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from fer import FER

# --- Initialization ---
app = Flask(__name__)
# Allow requests from your HTML file (Cross-Origin Resource Sharing)
CORS(app) 

# Initialize the Facial Emotion Recognition detector
# This will download the model weights the first time you run it.
# This is the step you could test in Colab!
try:
    emotion_detector = FER(mtcnn=True)
    print("Emotion detector loaded successfully.")
except Exception as e:
    print(f"Error loading emotion detector: {e}")
    emotion_detector = None

# --- Helper Functions ---
def base64_to_image(base64_string):
    """Converts a Base64 string from the frontend to an OpenCV image."""
    # Remove the "data:image/jpeg;base64," header
    if "," in base64_string:
        base64_string = base64_string.split(',')[1]
    
    # Decode the string and convert to a NumPy array
    img_data = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return image

def get_dominant_color(image, k=3):
    """Finds the most dominant color in an image, ignoring dull colors."""
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Reshape the image to be a list of pixels
    pixels = image_rgb.reshape((-1, 3))
    pixels = np.float32(pixels)

    # Apply K-Means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    centers = np.uint8(centers)
    
    # Get the count of each cluster
    _, counts = np.unique(labels, return_counts=True)
    
    # Find the most frequent color that is not too gray or dark
    dominant_color_hex = '#FFFFFF' # Default to white
    max_count = 0
    
    sorted_indices = np.argsort(counts)[::-1]

    for i in sorted_indices:
        color = centers[i]
        # Check if the color is vibrant enough (not too gray/dark)
        if (int(color[0]) + int(color[1]) + int(color[2])) > 150 and max(color) - min(color) > 25:
            dominant_color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            break # We found a good color
            
    return dominant_color_hex


def analyze_emotions(image):
    """Detects faces and analyzes their emotions."""
    if not emotion_detector:
        return "neutral" # Return neutral if detector failed to load

    # The FER library expects RGB, but OpenCV reads in BGR format. No conversion needed here.
    # The library handles it.
    analysis = emotion_detector.detect_emotions(image)

    if not analysis:
        return "neutral" # No face detected

    # Find the dominant emotion from the first detected face
    emotions = analysis[0]['emotions']
    dominant_emotion = max(emotions, key=emotions.get)
    
    # We only care about happy or sad for this project
    if dominant_emotion == 'happy':
        return 'happy'
    if dominant_emotion == 'sad':
        return 'sad'
        
    return 'neutral'


# --- API Endpoint ---
@app.route('/process_frame', methods=['POST'])
def process_frame():
    """Receives an image frame, analyzes it, and returns results."""
    try:
        data = request.get_json()
        image = base64_to_image(data['image'])

        if image is None:
            return jsonify({'error': 'Invalid image data'}), 400

        # --- Perform AI Analysis ---
        dominant_color = get_dominant_color(image)
        emotion = analyze_emotions(image)

        # --- Send Results Back to Frontend ---
        response = {
            'color': dominant_color,
            'emotion': emotion
        }
        return jsonify(response)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

# --- Main Execution ---
if __name__ == '__main__':
    print("Starting Flask server...")
    print("Open the index.html file in your browser after the server is running.")
    # Runs the server on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000)
