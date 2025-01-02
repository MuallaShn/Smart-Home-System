import os # İşletim sistemi işlemleri (dosya yolları gibi) için kullanılan kütüphane
import threading # Paralel iş parçacıkları oluşturmak için kullanılan kütüphane
from flask import Flask, jsonify  #Web uygulaması geliştirmek için kullanılan mikroframework
from flask_cors import CORS  # CORS: Farklı kaynaklardan gelen isteklere izin vermek için
from serialize import send_task

 
static_folder_path = os.path.abspath("../FRONTEND/myapp/build") # React uygulamasının build klasörünün yolu
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

# Cihazların durumlarını takip etmek için bir sözlük
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
    # Eğer cihaz açılacaksa
    if state == "turn_on": 
        device_status[device] = "turn_on"
    elif state == "turn_off": 
        device_status[device] = "turn_off"

    if device == "tv": #Kontrol edilen cihaz TV ise
       send_task()  # TV'ye özel bir komut gönder
    print(device, ":", state) # Konsola cihaz ve durumu yazdır
    return jsonify({"status": device, "command": state}) # JSON formatında cihaz durumu döndür


# Led durumunu sürekli kontrol eder
@app.route('/<device>/status', methods=['GET'])
def get_status(device):
    return jsonify({"command": device_status[device]}) #JSON formatında cihazın durumu belirtir

if __name__ == '__main__':
    # threading.Thread ile paralel bir iş parçacığı olarak çalıştırılır.
    threading.Thread(app.run(host='0.0.0.0', port=5000)).start()

