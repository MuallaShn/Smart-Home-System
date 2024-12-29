import serial
import time

def yolla_komutu(port = "COM5", baudrate = 9600 , tekrar_sayisi = 3):
    try:
        # Arduino ile seri bağlantıyı başlat
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Arduino'nun başlatılması için kısa bir süre bekleyin

        # Arduino'ya 'yolla X' komutunu gönder
        komut = f"yolla {tekrar_sayisi}\n"
        ser.write(komut.encode())  # Komutu gönder
        print(f"Gönderilen komut: {komut.strip()}")

        # Arduino'dan gelen yanıtları oku
        while True:
            yanit = ser.readline().decode().strip()
            if yanit:  # Eğer yanıt geldiyse
                print(f"Arduino'dan gelen: {yanit}")
            if "Gönderim tamamlandı." in yanit:  # Arduino'dan belirli bir yanıt alındığında çık
                break

        # Seri bağlantıyı kapat
        ser.close()
        print("Bağlantı kapatıldı.")
    except serial.SerialException as e:
        print(f"Seri bağlantı hatası: {e}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Kullanım
if __name__ == "__main__":
    # Arduino'nun bağlı olduğu portu ve baudrate değerini ayarlayın
    port = "COM5"  # Arduino'nun bağlı olduğu port (Windows için COMx, Linux/Mac için /dev/ttyUSBx)
    baudrate = 9600  # Arduino ile aynı baudrate
    tekrar_sayisi = 3  # Kaç kez sinyal gönderileceğini belirleyin

    # Komut fonksiyonunu çağırın
    yolla_komutu(port, baudrate, tekrar_sayisi)
