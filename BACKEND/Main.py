import os
import threading
import time
from flask import Flask, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Flask uygulaması
static_folder_path = os.path.abspath("../FRONTEND/myapp/build")
app = Flask(__name__, static_folder=static_folder_path, static_url_path="/")
CORS(app)

# Global değişkenler
voice_control_active = False
voice_thread = None
led_status = "kapalı"

def speak(text):
    """Metni sesli olarak okur."""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        playsound("output.mp3")
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
    """Sesli kontrol sistemi."""
    global voice_control_active, led_status
    while voice_control_active:
        try:
            command = listen_command("Alexa komutunu bekliyorum...")
            print(f"Algılanan komut: {command}")
            
            if command and "alexa" in command:
                print("Alexa komutu algılandı.")
                speak("efendim mualla, esra, beytullah, abdulkadir dinliyorum")
                
                action = listen_command("Komutunuzu söyleyin...")
                print(f"Algılanan aksiyon: {action}")
                
                if action:
                    if "led aç" in action:
                        led_status = "açık"
                        print("LED açılıyor...")
                        speak("LED açıldı.")
                    elif "led kapa" in action:
                        led_status = "kapalı"
                        print("LED kapatılıyor...")
                        speak("LED kapatıldı.")
                    elif "kapat" in action:
                        print("Sesli komut sistemi kapatılıyor...")
                        speak("Sesli komut sistemi kapatılıyor.")
                        voice_control_active = False
                        break
                    else:
                        print(f"Bilinmeyen komut: {action}")
                        speak("Komutu anlayamadım. Lütfen tekrar deneyin.")
                else:
                    print("Komut algılanamadı.")
                    speak("Komut algılanamadı. Lütfen tekrar deneyin.")
                
                # Bekleme süresi ekle
                print("Bir sonraki komut için bekleniyor...")
                time.sleep(5)  # Bekleme süresi (5 saniye)
            else:
                print("Alexa komutu algılanmadı. Döngüye devam ediliyor...")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            speak("Bir hata oluştu. Lütfen tekrar deneyin.")

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

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print(f"Ngrok Public URL: {public_url}")
    app.run(host="0.0.0.0", port=5000)

