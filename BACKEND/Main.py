# import os
# from flask import Flask, send_from_directory, request, jsonify
# from flask_cors import CORS
# from pyngrok import ngrok

# #Reactın build alındığı dosya
# static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
# app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
# CORS(app)

# #Ledin durumunu kontrol ediyor
# led_status ={
#     "pc":"turn_off",
#     "tv":"turn_off",
#     "light1":"turn_off",
#     "light2":"turn_off",
#     "light3":"turn_off",
#     "light4":"turn_off"
# }

# #Ana sayfa
# @app.route("/")
# def index():
#     return send_from_directory(app.static_folder, "index.html")


# #Cihazların durumunu kontrol ettiğimiz metod
# @app.route("/<device>/<state>", methods=["POST", "GET"])
# def device_control(device,state):
#     global led_status
#     if state=="turn_on":
#         led_status = "yak"
#     elif state=="turn_off":
#         led_status="kapa"
#     print(device ,":" ,state)
#     return jsonify({"status": device, "command": state})


# #Led durumunu sürekli kontrol eder
# @app.route('/<device>/status', methods=['GET'])
# def get_status(device):
#     return jsonify({"command":device})
#     #return jsonify({"command": led_status})

# if __name__ == '__main__':
#     public_url = ngrok.connect(5000)
#     #print(f"Ngrok Public URL: {public_url}")
#     app.run(host='0.0.0.0', port=5000)

# import os
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from pyngrok import ngrok
# import threading
# import speech_recognition as sr
# import pyttsx3

# static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
# app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
# CORS(app)


# # Global değişkenler
# led_status = "kapalı"
# voice_control_active = False
# voice_thread = None

# # Konuşma motoru ayarları
# engine = pyttsx3.init()
# engine.setProperty("rate", 200)
# engine_lock = threading.Lock()

# def speak(text):
#     with engine_lock:
#         engine.say(text)
#         engine.runAndWait()

# def listen_command(prompt="Dinliyorum..."):
#     """Kullanıcıdan sesli komut alır."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print(prompt)
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#             command = recognizer.recognize_google(audio, language="tr-TR")
#             print(f"Algılanan komut: {command}")
#             return command.lower()
#         except sr.WaitTimeoutError:
#             print("Zaman aşımı.")
#         except sr.UnknownValueError:
#             print("Anlaşılamadı.")
#         except sr.RequestError:
#             print("Ses tanıma servisine ulaşılamadı.")
#         return None

# @app.route("/")
# def index():
#     """React uygulamasının ana sayfasını döndürür."""
#     return app.send_static_file("index.html")

# def voice_control():
#     """Sesli kontrol sistemi."""
#     global voice_control_active, led_status
#     while voice_control_active:
#         command = listen_command("Alexa komutunu bekliyorum...")
#         if command and "alexa" in command:
#             with engine_lock:
#                 speak("Evet, dinliyorum.")
#             action = listen_command("Komutunuzu söyleyin...")
#             if action:
#                 if "led aç" in action:
#                     led_status = "açık"
#                     with engine_lock:
#                         speak("LED açıldı.")
#                 elif "led kapa" in action:
#                     led_status = "kapalı"
#                     with engine_lock:
#                         speak("LED kapatıldı.")
#                 elif "kapat" in action:
#                     with engine_lock:
#                         speak("Sesli komut sistemi kapatılıyor.")
#                     voice_control_active = False
#                     break
#                 else:
#                     with engine_lock:
#                         speak("Komutu anlayamadım.")

# @app.route("/led/status", methods=["GET"])
# def get_led_status():
#     """LED durumunu döndürür."""
#     return jsonify({"status": led_status})


# @app.route("/led/toggle", methods=["POST"])
# def toggle_led():
#     """LED durumunu değiştirir ve mesaj döndürür."""
#     global led_status
#     if led_status == "kapalı":
#         led_status = "açık"
#         message = "LED açıldı"
#     else:
#         led_status = "kapalı"
#         message = "LED kapatıldı"

#     # Terminale mesaj yazdır
#     print(f"LED durumu değişti: {message}")

#     # JSON formatında mesaj döndür
#     return jsonify({"status": led_status, "message": message})


# @app.route("/voice/toggle", methods=["POST"])
# def toggle_voice_control():
#     """Sesli kontrolü başlatır veya kapatır."""
#     global voice_control_active, voice_thread
#     if not voice_control_active:
#         voice_control_active = True
#         voice_thread = threading.Thread(target=voice_control, daemon=True)
#         voice_thread.start()
#         return jsonify({"status": "Sesli komut sistemi başlatıldı."})
#     else:
#         voice_control_active = False
#         return jsonify({"status": "Sesli komut sistemi kapatıldı."})


# if __name__ == "__main__":
#     public_url = ngrok.connect(5000)
#     print(f"Ngrok Public URL: {public_url}")
#     app.run(host="0.0.0.0", port=5000)

import os
import threading
import time
import serial
from flask import Flask, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import speech_recognition as sr
from gtts import gTTS
# from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Flask uygulaması
static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

# Global değişkenler
voice_control_active = False
voice_thread = None

led_status = {
    "pc": "turn_off",
    "tv": "turn_off",
    "light1": "turn_off",
    "light2": "turn_off",
    "light3": "turn_off",
    "light4": "turn_off"
}

arduino = None
led1 = False


def speak(text):
    """Metni sesli olarak okur."""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        # playsound("output.mp3")
        os.remove("output.mp3")  # Geçici dosyayı sil
    except Exception as e:
        print(f"Sesi oynatırken hata oluştu: {e}")


def listen_command(prompt="Dinliyorum..."):
    """Mikrofondan sesli komut alır."""
    recognizer = sr.Recognizer()
    print(prompt)
    try:
        # Mikrofon kaynağı açılır ve otomatik olarak kapatılır
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Mikrofon dinleniyor...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
        # Komut algılanıyor
        command = recognizer.recognize_google(audio, language="tr-TR")
        print(f"Algılanan komut: {command}")
        return command.lower()
    except sr.WaitTimeoutError:
        print("Zaman aşımı: Hiçbir ses algılanmadı.")
        return None
    except sr.UnknownValueError:
        print("Anlaşılamadı: Ses algılandı ancak anlaşılamadı.")
        return None
    except sr.RequestError as e:
        print(f"Google API Hatası: {e}")
        return None
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        return None


def voice_control():
    global led1
    """Sesli kontrol sistemi."""
    global voice_control_active, led_status
    while voice_control_active:
        try:
            command = listen_command("Alexa komutunu bekliyorum...")
            print(f"Algılanan komut: {command}")

            if command and "alexa" in command:
                print("Alexa komutu algılandı.")
                speak("Yes, i am listening")

                action = listen_command("Komutunuzu söyleyin...")
                print(f"Algılanan aksiyon: {action}")

                if action:
                    if "led aç" in action:
                        led_status["light1"] = "turn_on"
                        led1 = True
                        print("LED açılıyor...")
                        speak("LED turned on.")
                    elif "led kapa" in action:
                        led_status["light1"] = "turn_off"
                        led1 = False
                        print("LED kapatılıyor...")
                        speak("LED turned off.")
                    elif "kapat" in action:
                        print("Sesli komut sistemi kapatılıyor...")
                        speak("Shutting down the voice command system.")
                        voice_control_active = False
                        break
                    else:
                        print(f"Bilinmeyen komut: {action}")
                        speak("I don't understand the command, please try again.")
                else:
                    print("Komut algılanamadı.")
                    speak("The command could not be detected. Please try again.")

                # Bekleme süresi ekle
                print("Bir sonraki komut için bekleniyor...")
                time.sleep(5)  # Bekleme süresi (5 saniye)
            else:
                print("Alexa komutu algılanmadı. Döngüye devam ediliyor...")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            speak("An error has occurred. Please try again.")


@app.route("/")
def index():
    """React uygulamasının ana sayfasını döndürür."""
    return app.send_static_file("index.html")


@app.route("/voice/toggle", methods=["POST"])
def toggle_voice_control():
    """Sesli kontrolü başlatır veya kapatır."""
    global voice_control_active, voice_thread
    if not voice_control_active:
        voice_control_active = True
        voice_thread = threading.Thread(target=voice_control, daemon=True)
        voice_thread.start()
        return jsonify({"status": "Sesli komut sistemi başlatıldı."})
    else:
        voice_control_active = False
        return jsonify({"status": "Sesli komut sistemi kapatıldı."})


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


def connect_serial_port():
    global arduino
    try:
        arduino = serial.Serial(
            port='COM6',
            baudrate=9600,
            timeout=1
        )
        print(f"Arduino'ya bağlandı: {arduino.port}")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        exit()


def send_task(task):
    global arduino
    try:
        arduino.write(f"{task}\n".encode())
        time.sleep(0.5)
    except Exception as e:
        print(f"hata {e}")
        arduino.close()


def selenium():
    global led1
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get("http://127.0.0.1:5000")
        print("bağlandı")
        while True:
            if led1:
                print("skdnfds")
                driver.find_element(by=By.XPATH,
                                    value='//*[@id="devices"]/div/div/div[3]/div/div/div/button[1]').click()
                led1 = False

    except Exception as e:
        print(f"Selenium başlatılırken hata oluştu: {e}")


if __name__ == '__main__':
    # public_url = ngrok.connect("5000")
    # connect_serial_port()
    # threading.Thread(target=send_task("LED_ON")).start()
    threading.Thread(target=selenium, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)


