import cv2
from transformer import transform
from PIL import Image
from predict import predict

# Load pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Function to detect faces in the given frame
def extract_faces(frame):
    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to extract and transform the face image to a tensor
def extract_transformed_image_from_face(face):
    # Convert the face (OpenCV image) to a PIL image (RGB format)
    face_pil = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
    # Apply transformation and return the transformed tensor
    _, face_tensor = transform(face_pil)
    face_tensor = face_tensor
    return face_tensor

# Function to draw a rectangle around the face and display the predicted emotion with confidence
def draw_rectangle_with_emotion(frame, emotion, percentage, x, y, w, h) -> None:
    # Draw a green rectangle around the detected face
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Display the emotion and confidence percentage near the face
    cv2.putText(frame, f'{emotion}: {percentage:.2f}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

# Function to process a frame and detect emotions in faces
def process_frame(frame):
    # For each detected face, extract the face, predict emotion, and draw a rectangle with the result
    for (x, y, w, h) in extract_faces(frame):
        face = frame[y:y + h, x:x + w]
        transformed_face = extract_transformed_image_from_face(face)
        # Get the predicted emotion and percentages
        emotion, percentages = predict(transformed_face)
        # Draw the emotion and rectangle on the frame
        draw_rectangle_with_emotion(frame, emotion, percentages[emotion], x, y, w, h)
