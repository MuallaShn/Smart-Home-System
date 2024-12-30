import serial
import time

def send_task():

    try:
        # Arduino'nun bağlı olduğu portu ve baudrate değerini atadık
        port = "COM5"
        baudrate = 9600
        # Kaç kez sinyal gönderileceğini belirledik
        tekrar_sayisi = 3

        # Arduino ile seri bağlantıyı başlatır ve iki saniye bekler
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

        # Arduino'ya komut gönderir
        komut = f"yolla {tekrar_sayisi}\n"
        ser.write(komut.encode())  # Komutu gönder
        print(f"Gönderilen komut: {komut.strip()}")

        # Arduino'dan gelen yanıtları okur
        while True:
            response = ser.readline().decode().strip()
            if response:
                print(f"Arduino'dan gelen: {response}")
            # Arduino'dan belirli bir yanıt alındığında çıkar
            if "Gönderim tamamlandı." in response:
                break

        # Seri bağlantıyı kapatır
        ser.close()
        print("Bağlantı kapatıldı.")
    except serial.SerialException as e:
        print(f"Seri bağlantı hatası: {e}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    # Komut fonksiyonunu çağırdık
    send_task()
