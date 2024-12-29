import time
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
from gtts import gTTS
import pygame
import os
from gptUtils import chat_with_ollama
import requests  # HTTP istekleri için gerekli kütüphane

# Vosk model yolunu belirleyin
model_path = "model_tr"  # İndirdiğiniz Vosk modelinin klasör yolu

# Flask sunucusunun URL'si (ngrok tarafından sağlanan URL)
FLASK_SERVER_URL = "http://127.0.0.1:5000"  # Flask uygulamanızın çalıştığı adres

# Modeli yükle
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)  # 16kHz örnekleme hızı için yapılandırma

# Ses verisini paylaşmak için bir kuyruk (queue)
audio_queue = queue.Queue()


def audio_callback(indata, frames, time, status):
    """Mikrofon girişinden alınan ses verisini kuyruğa ekler."""
    if status:
        print(f"Hata: {status}", flush=True)
    audio_queue.put(bytes(indata))  # Veriyi kuyruğa ekle


def play_audio(text):
    """Metni sesli olarak oynatır."""
    tts = gTTS(text=text, lang="tr")
    tts.save("response.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    os.remove("response.mp3")


def control_light(device, state):
    """Flask sunucusuna cihaz durumu güncelleme isteği gönderir."""
    try:
        url = f"{FLASK_SERVER_URL}/{device}/{state}"
        response = requests.post(url)
        if response.status_code == 200:
            print(f"{device} başarıyla {state} edildi.")
        else:
            print(f"{device} için durum değişikliği başarısız: {response.status_code}")
    except Exception as e:
        print(f"LED durumu güncellenemedi: {e}")


def listen_and_respond():
    print("Ayşe dediğinizde cümlenizi dinleyeceğim. Dinliyorum...")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback) as stream:
        while True:
            # Kuyruktan ses verisini al
            audio_data = audio_queue.get()

            # Vosk ile analiz et
            if recognizer.AcceptWaveform(audio_data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").lower()

                if "ayşe" in text:
                    print("Ayşe dendi. Cümlenizi dinliyorum...")

                    # Mikrofondan veri almayı durdur
                    stream.stop()
                    play_audio("Dinliyorum")  # Dinleme öncesi bekleme süresi
                    stream.start()  # Ses çalması tamamlandıktan sonra yeniden başlat

                    # Yeni bir cümle bekle
                    while True:
                        audio_data = audio_queue.get()
                        if recognizer.AcceptWaveform(audio_data):
                            result = json.loads(recognizer.Result())
                            sentence = result.get("text", "").lower()
                            if sentence:
                                if sentence == "birinci yak":
                                    play_audio("Priz açılıyor")
                                    control_light("light1", "turn_on")
                                elif sentence == "birinci kapat":
                                    play_audio("Priz kapatılıyor")
                                    control_light("light1", "turn_off")
                                else:
                                    print(f"Duyulan cümle: {sentence}")
                                    response = chat_with_ollama(sentence)
                                    print(f"Ollama Yanıtı: {response}")
                                    play_audio(response)
                                break


if __name__ == "__main__":
    try:
        listen_and_respond()
    except KeyboardInterrupt:
        print("Dinleme durduruldu.")
    except Exception as e:
        print(f"Hata: {e}")
