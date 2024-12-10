from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False 


led_status = "kapa" 

@app.route('/yak', methods=['GET'])
def yak_led():
    global led_status
    led_status = "yak"  
    print("Komut: LED YAK")
    return jsonify({"status": "LED YAK", "command": "yak"})

@app.route('/kapa', methods=['GET'])
def kapa_led():
    global led_status
    led_status = "kapa"  
    print("Komut: LED SÖNDÜR")
    return jsonify({"status": "LED SÖNDÜR", "command": "kapa"})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"command": led_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
