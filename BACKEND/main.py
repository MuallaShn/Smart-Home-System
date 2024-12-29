import os
import threading
from flask import Flask, jsonify
from flask_cors import CORS
from serialize import yolla_komutu


static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

device_status = {
    "pc": "turn_on",
    "light1": "turn_off",
    "light2": "turn_off",
    "light3": "turn_off",
    "light4": "turn_off",
}
@app.route("/")
def index():
    """React uygulamasının ana sayfasını döndürür."""
    return app.send_static_file("index.html")


# Cihazların durumunu kontrol ettiğimiz metod
@app.route("/<device>/<state>", methods=["POST", "GET"])
def device_control(device, state):
    global device_status
    if state == "turn_on":
        device_status[device] = "turn_on"
    elif state == "turn_off":
        device_status[device] = "turn_off"

    if device == "tv":
        yolla_komutu()
    print(device, ":", state)
    return jsonify({"status": device, "command": state})


# Led durumunu sürekli kontrol eder
@app.route('/<device>/status', methods=['GET'])
def get_status(device):
    return jsonify({"command": device_status[device]})

if __name__ == '__main__':
    threading.Thread(app.run(host='0.0.0.0', port=5000)).start()

