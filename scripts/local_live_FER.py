import cv2
from live_FER import process_frame

cap = cv2.VideoCapture(0)


def live_tracking_FER() -> None:
    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        process_frame(frame)

        cv2.imshow("Live Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main() -> None:
    if not cap.isOpened():
        print("Error: Unable to access webcam.")
        exit()

    live_tracking_FER()


if __name__ == '__main__':
    main()
