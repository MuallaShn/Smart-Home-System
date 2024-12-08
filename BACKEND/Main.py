import asyncio
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

# Flask uygulaması
app = Flask(__name__, static_folder="../FRONTEND/myapp/build", static_url_path="/")
CORS(app)
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/turn_on", methods=["POST"])
def turn_on():
    print("ışık açıldı")
    return send_from_directory(app.static_folder, "index.html")

def run_flask():
    app.run(port=5000, host="127.0.0.1", debug=True, use_reloader=False)

async def main():
    await asyncio.gather(
        asyncio.to_thread(run_flask)
    )

if __name__ == "__main__":
    asyncio.run(main())
