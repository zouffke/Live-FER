import cv2
import numpy as np
import base64

from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request, jsonify, render_template

from live_FER import process_frame

app = Flask(__name__)

asgi_app = WsgiToAsgi(app)

@app.route('/process_frame', methods=['POST'])
def process_frame_request():
    try:
        # Log the raw data to check the structure
        data = request.get_json()

        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # Get the base64-encoded image string from the request
        image_data = data['image']
        image_data = image_data.split(',')[1]  # Remove the prefix 'data:image/jpeg;base64,'
        img_bytes = base64.b64decode(image_data)

        # Convert bytes to numpy array and then decode to frame
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({'error': 'Failed to decode image'}), 500

        # Process the frame (add face detection, emotion prediction, etc.)
        process_frame(frame)

        # Encode the processed frame back to JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        if not _:
            return jsonify({'error': 'Failed to encode processed image'}), 500

        processed_frame_base64 = base64.b64encode(buffer).decode('utf-8')

        # Return the processed image as a base64 string
        return jsonify({'image': f'data:image/jpeg;base64,{processed_frame_base64}'}), 200

    except Exception as e:
        return jsonify({'error': f'Error processing frame: {e}'}), 500



@app.route('/')
def index():
    return render_template('index.html')  # Renders the index page

if __name__ == '__main__':
    app.run(port=5000)
