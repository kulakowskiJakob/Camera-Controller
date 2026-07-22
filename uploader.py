import json
import time
import requests

class Uploader:

    def __init__(self, url):
        self.url = url

    def upload(self, image, frame_id):

        metadata = {
            "timestamp": time.time(),
            "frame_id": frame_id,
            "resolution": "1280x720"
        }

        files = {
            "files": ("frame.jpg", image, "image/jpeg")
        }

        data = {
            "metadata": json.dumps(metadata)
        }

        requests.post(
            self.url,
            files=files,
            data=data
        )