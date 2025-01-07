// Access the video element
const video = document.createElement("video");
video.width = 640;
video.height = 480;
video.autoplay = true;

// Set up the video stream from the browser's camera
navigator.mediaDevices.getUserMedia({video: true})
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(error => {
        console.error('Error accessing the camera: ', error);
    });

// Capture frames and send them to the Flask server for processing
function captureAndSendFrame() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw the current video frame onto the canvas, cropping the desired area
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert the canvas to a base64 image
    const frameData = canvas.toDataURL('image/jpeg');

    // Send the frame to the Flask server via fetch
    fetch('/process_frame', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({image: frameData})
    })
        .then(response => response.json())  // Ensure you parse the response as JSON
        .then(data => {
            if (data.image) {
                const img = document.getElementById("canvas");
                img.src = data.image;  // Set the processed image from the server
            } else {
                console.error('No image field in the response:', data);
            }
        })
        .catch(error => {
            console.error('Error processing frame:', error);
        });
}

// Call captureAndSendFrame every 100ms to continuously send frames for processing
setInterval(captureAndSendFrame, 100);

// Fullscreen toggle logic
const fullscreenButton = document.getElementById('fullscreen-btn');
fullscreenButton.addEventListener('click', () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch((err) => {
            console.error(`Error attempting to enable fullscreen mode: ${err.message}`);
        });
    } else {
        document.exitFullscreen().catch((err) => {
            console.error(`Error attempting to exit fullscreen mode: ${err.message}`);
        });
    }
});
