from picamera2 import Picamera2
import cv2

class Camera:

    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height

        self.camera = Picamera2()
        config = self.camera.create_video_configuration(
            main={"size": (width, height),
                  "format": "RGB888"
            }
        )

        self.camera.configure(config)
        self.camera.start()

        self.frame_id = 0

    def capture(self):
        frame = self.camera.capture_array()

        self.frame_id += 1
        return frame
    
    def get_jpeg(self):
        frame = self.capture()
        _, jpeg = cv2.imencode(".jpg", frame)

        return jpeg.tobytes()
    
    def stop(self):
        self.camera.stop()

        
