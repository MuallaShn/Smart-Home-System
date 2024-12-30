import requests
import os
import time

def check_and_shutdown():
    url = "http://192.168.137.1:5000/pc/status"
    try:
        while True:
            response = requests.get(url)
            # yanıtı kontrol eder
            if response.status_code == 200:
                #json formatında olan veriyi alır ve command değerini pc_statuse atar
                data = response.json()
                pc_status = data.get("command")


                print(f"PC Durumu: {pc_status}")

                # eğer status turn_off ise pcyi uyku moduna alır
                if pc_status == "turn_off":
                    print("Bilgisayar kapatılıyor...")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    break
            else:
                print(f"Hata: {response.status_code} - {response.text}")


            time.sleep(1)

    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

if __name__== "__main__":
    check_and_shutdown()
