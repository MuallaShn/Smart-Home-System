import os
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok

#Reactın build alındığı dosya
static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

#Ledin durumunu kontrol ediyor
led_status ={
    "pc":"turn_off",
    "tv":"turn_off",
    "light1":"turn_off",
    "light2":"turn_off",
    "light3":"turn_off",
    "light4":"turn_off"
}

#Ana sayfa
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


#Cihazların durumunu kontrol ettiğimiz metod
@app.route("/<device>/<state>", methods=["POST", "GET"])
def device_control(device,state):
    global led_status
    if state=="turn_on":
        led_status = "yak"
    elif state=="turn_off":
        led_status="kapa"
    print(device ,":" ,state)
    return jsonify({"status": device, "command": state})


#Led durumunu sürekli kontrol eder
@app.route('/<device>/status', methods=['GET'])
def get_status(device):
    return jsonify({"command":device})
    #return jsonify({"command": led_status})

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    #print(f"Ngrok Public URL: {public_url}")
    app.run(host='0.0.0.0', port=5000)