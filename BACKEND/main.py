import os
import threading
from flask import Flask, jsonify
from flask_cors import CORS
from pyngrok import ngrok

static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

# Global değişkenler
voice_control_active = False
voice_thread = None
user_name = None

led_status = {
    "pc": "turn_on",
    "light1": "turn_off",
    "light2": "turn_off",
    "light3": "turn_off",
    "light4": "turn_off"
}



@app.route("/")
def index():
    """React uygulamasının ana sayfasını döndürür."""
    return app.send_static_file("index.html")


@app.route("/voice/toggle", methods=["POST"])
def toggle_voice_control():
    print("za")
    return jsonify({"status": voice_control_active})


# Cihazların durumunu kontrol ettiğimiz metod
@app.route("/<device>/<state>", methods=["POST", "GET"])
def device_control(device, state):
    global led_status
    if state == "turn_on":
        led_status[device] = "turn_on"
    elif state == "turn_off":
        led_status[device] = "turn_off"
    print(device, ":", state)
    return jsonify({"status": device, "command": state})


# Led durumunu sürekli kontrol eder
@app.route('/<device>/status', methods=['GET'])
def get_status(device):
    return jsonify({"command": led_status[device]})
    # return jsonify({"command": led_status})





if __name__ == '__main__':
    # public_url = ngrok.connect("5000")
    # connect_serial_port()
    # threading.Thread(target=send_task("LED_ON")).start()
    threading.Thread(app.run(host='0.0.0.0', port=5000)).start()

