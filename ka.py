from flask import Flask, Response
import cv2

app = Flask(__name__)

# RTSP URL ka use karke camera se video stream fetch karna
camera_url = "rtsp://admin:12345@192.168.1.10:554/live"
cap = cv2.VideoCapture(camera_url)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
