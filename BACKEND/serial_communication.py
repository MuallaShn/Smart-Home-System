import serial
import time

arduino = None


def connect_serial_port(port='COM6', baudrate=9600):
    """Arduino ile bağlantı kurar."""
    global arduino
    try:
        arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        print(f"Arduino'ya bağlandı: {arduino.port}")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        exit()


def send_task(task):
    """Arduino'ya komut gönderir."""
    global arduino
    try:
        if arduino:
            arduino.write(f"{task}\n".encode())
            time.sleep(0.5)
    except Exception as e:
        print(f"Hata: {e}")
        arduino.close()
