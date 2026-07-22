from flask import Response

class Streamer:

    def __init__(self, camera):
        self.camera = camera

    def generate(self):

        while True:

            frame = self.camera.get_jpeg()

            yield (
                b' --frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'
                + frame +
                b'\r\n'
            )
    def response(self):

        return Response(
            self.generate(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
        )