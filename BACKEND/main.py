import os
import threading
from flask import Flask, jsonify
from flask_cors import CORS
from serialize import send_task


static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

#her bir cihazın adı ve varsayılan değerleri
device_status = {
    "pc": "turn_on",
    "light1": "turn_off",
    "light2": "turn_off",
    "light3": "turn_off",
    "light4": "turn_off",
}

# ana sayfayı döndürür
@app.route("/")
def index():
    return app.send_static_file("index.html")


# cihaz ve durumu şeklinde iki adet parametre alarak cihazların durumunu kontrol eder
@app.route("/<device>/<state>", methods=["POST", "GET"])
def device_control(device, state):
    global device_status
    if state == "turn_on":
        device_status[device] = "turn_on"
    elif state == "turn_off":
        device_status[device] = "turn_off"

    #eğer cihaz televizyonsa send_task komutuna git
    if device == "tv":
        send_task()
    print(device, ":", state)
    return jsonify({"status": device, "command": state})


# Led durumunu sürekli kontrol eder
@app.route('/<device>/status', methods=['GET'])
def get_status(device):
    return jsonify({"command": device_status[device]})

if __name__ == '__main__':
    threading.Thread(app.run(host='0.0.0.0', port=5000)).start()

