import os
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok

# Statik dosya yolunu ayarla
static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)


led_status = "kapa"

@app.route("/")
def serve():
    
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<device>/<state>", methods=["POST", "GET"])
def turn_on(device,state):
    global led_status
    led_status = "yak"
    print(device ,":" ,state)
    return jsonify({"status": device, "command": state})

@app.route("/light/turn_off", methods=["POST", "GET"])
def turn_off():
    global led_status
    led_status = "kapa"
    print("Komut: LED SÖNDÜR")
    return jsonify({"status": "LED ", "command": "kapa"})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"command": led_status})

if __name__ == '__main__':
    
    public_url = ngrok.connect(5000)
    print(f"Ngrok Public URL: {public_url}")

    
    app.run(host='0.0.0.0', port=5000)