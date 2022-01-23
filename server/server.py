import os
from io import BytesIO

from flask import Flask, send_file, request

from composer_7 import ImageComposer7

app = Flask(__name__)


@app.route("/")
def index():
    config = {
        "latitude": "50.838557",
        "longitude": "-0.767475",
        "timezone": "Europe/London",
        "country": "gb",
        "font": "Roboto",
    }
    if os.environ.get("CONFIG"):
        import json
        config = json.load(open(os.environ.get("CONFIG")))
    config.update(request.args)

    # Get API key
    api_key = config.get("api_key")
    if not api_key:
        return '{"error": "no_api_key"}'
    # Render
        
    composer = ImageComposer7(**config)
    output = composer.render()
    
    output.seek(0)
    return send_file(output, mimetype="image/png")
