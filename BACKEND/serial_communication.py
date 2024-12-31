import serial # Seri port üzerinden iletişim kurmak için kullanılan kütüphane
import time

# Arduino bağlantısını temsil eden değişken (başlangıçta boş)
arduino = None


def connect_serial_port(port='COM6', baudrate=9600):
    """Arduino ile bağlantı kurar."""
    global arduino
    try:
        # Arduino ile bağlantı kurulur
        arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        print(f"Arduino'ya bağlandı: {arduino.port}") # Bağlantı başarılı olduğunda bilgilendirme mesajı
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        exit()


def send_task(task):
    """Arduino'ya komut gönderir."""
    global arduino
    try:
        if arduino:
            arduino.write(f"{task}\n".encode())# Komut metni UTF-8 formatına dönüştürülüp gönderilir
            time.sleep(0.5) # Gönderim sonrası kısa bir bekleme süresi
    except Exception as e:
        print(f"Hata: {e}")
        arduino.close()
