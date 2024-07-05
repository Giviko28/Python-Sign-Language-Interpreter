import base64
import io
from PIL import Image
from flask import Flask, request, jsonify, render_template_string, render_template
from dookie_api import analyze_frame
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_image", methods=["POST"])
def process_image_endpoint():
    data = request.get_json()
    if data and "image" in data:
        image_data = data["image"].split(",")[1]
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        result = analyze_frame(image)
        return jsonify({"result": result})

    return jsonify({"error": "No image data found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
