#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "alexa";
const char* password = "alexa123";

const char* serverURL = "http://192.168.137.1:5000";


#define LED_PIN1 D1
#define LED_PIN2 D2
#define LED_PIN3 D3
#define LED_PIN4 D4


WiFiClient client;

void setup() {
  Serial.begin(9600);


  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  pinMode(LED_PIN4, OUTPUT);

  digitalWrite(LED_PIN1, LOW);
  digitalWrite(LED_PIN2, LOW);
  digitalWrite(LED_PIN3, LOW);
  digitalWrite(LED_PIN4, LOW);

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

void kontrolEt(const char* endpoint, int ledPin) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String(serverURL) + endpoint;
    http.begin(client, url);
    int httpCode = http.GET();

    if (httpCode > 0) {
      String payload = http.getString();
      Serial.println("Yanıt: " + payload);

      if (payload.indexOf("\"command\":\"turn_on\"") > 0) {
        digitalWrite(ledPin, HIGH); // LED yak
        Serial.println("LED YAK");
      } else if (payload.indexOf("\"command\":\"turn_off\"") > 0) {
        digitalWrite(ledPin, LOW); // LED kapa
        Serial.println("LED SÖNDÜR");
      }
    } else {
      Serial.println("HTTP Bağlantı Hatası");
    }
    http.end();
  }
}

void loop() {
  kontrolEt("/light1/status", LED_PIN1);
  kontrolEt("/light2/status", LED_PIN2);
  kontrolEt("/light3/status", LED_PIN3);
  kontrolEt("/light4/status", LED_PIN4);

  delay(500);
}
