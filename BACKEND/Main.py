import asyncio
from flask import Flask, send_from_directory, request, jsonify

# Flask uygulaması
app = Flask(__name__, static_folder="../FRONTEND/myapp/build", static_url_path="/")
app.config['JSON_AS_ASCII'] = False


led_status = "kapa"
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/turn", methods=["POST","GET"])
def turn_on():
    global led_status
    led_status = "yak"
    print("Komut: LED YAK")
    return jsonify({"status": "LED YAK", "command": "yak"})


@app.route("/turn_off", methods=["POST","GET"])
def turn_off():
    global led_status
    led_status = "kapa"
    print("Komut: LED SÖNDÜR")
    return jsonify({"status": "LED ", "command": "kapa"})



@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"command": led_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

