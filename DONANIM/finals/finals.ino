#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// Wi-Fi bilgileri
const char* ssid = "alexa";      // Wi-Fi ağ adınızı buraya yazın
const char* password = "alexa123";  // Wi-Fi şifrenizi buraya yazın

// Flask sunucusunun IP adresi ve portu
const char* serverURL = "http://192.168.137.1:5000/status"; // Flask sunucusunun IP adresini güncelleyin

// LED pin tanımı
#define LED_PIN2 D5
#define LED_PIN D6
#define LED_PIN3 D7
#define LED_PIN4 D8

// Wi-Fi istemcisi
WiFiClient client;

void setup() {
  Serial.begin(9600);

  // LED pini çıkış olarak ayarla
  pinMode(LED_PIN, OUTPUT); // LED başlangıçta kapalı
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  pinMode(LED_PIN4, OUTPUT);

  digitalWrite(LED_PIN, LOW);
  digitalWrite(LED_PIN2, LOW);
  digitalWrite(LED_PIN3, LOW);
  digitalWrite(LED_PIN4, LOW);
  // Wi-Fi bağlantısını başlat
  Serial.println("Wi-Fi'ye bağlanılıyor...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi'ye bağlanıldı!");
  Serial.print("IP Adresi: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Flask sunucusundaki /status endpoint'ine bağlan
    http.begin(client, serverURL);
    int httpCode = http.GET();

    if (httpCode > 0) {
      String payload = http.getString(); // Sunucudan gelen yanıtı al
      Serial.println("Sunucudan Gelen Yanıt: " + payload);
      // Gelen yanıtı kontrol et
      if (payload.indexOf("\"command\":\"yak\"") > 0) {  // 'yak' komutu
        digitalWrite(LED_PIN, HIGH); // LED'i yak
        Serial.println("LED YAK");
      } else if (payload.indexOf("\"command\":\"kapa\"") > 0) {  // 'kapa' komutu
        digitalWrite(LED_PIN, LOW); // LED'i söndür
        Serial.println("LED SÖNDÜR");
      }
    } else {
      Serial.println("HTTP Bağlantı Hatası");
    }
    http.end(); // HTTP bağlantısını sonlandır
  }

  delay(1000); // 1 saniyede bir sunucuyu kontrol et
}
