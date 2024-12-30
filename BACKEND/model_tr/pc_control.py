import requests
import os
import time

def check_and_shutdown():
    url = "http://192.168.137.1:5000/pc/status"
    try:
        while True:
            response = requests.get(url)

            # Yanıtı kontrol et
            if response.status_code == 200:
                data = response.json()
                pc_status = data.get("command")

                print(f"PC Durumu: {pc_status}")

                # PC "turn_off" durumundaysa bilgisayarı kapat
                if pc_status == "turn_off":
                    print("Bilgisayar kapatılıyor...")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    break
            else:
                print(f"Hata: {response.status_code} - {response.text}")


            time.sleep(1)

    except requests.RequestException as e:
        print(f"HTTP isteği sırasında bir hata oluştu: {e}")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

if __name__== "__main__":
    check_and_shutdown()
