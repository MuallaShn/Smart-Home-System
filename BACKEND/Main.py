import asyncio
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

# Flask uygulaması
app = Flask(__name__, static_folder="../FRONTEND/myapp/build", static_url_path="/")



led_status = "kapa"
CORS(app)

app.config['JSON_AS_ASCII'] = False
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
    return jsonify({"status": "LED SÖNDÜR", "command": "kapa"})


def run_flask():
    app.run(port=5000, host="0.0.0.0", debug=True, use_reloader=False)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"command": led_status})

async def main():
    await asyncio.gather(
        asyncio.to_thread(run_flask)
    )

if __name__ == "__main__":
    asyncio.run(main())
