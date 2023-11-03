#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <ctime>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
#define BTN_PIN 5
#define TFT_DC 2
#define TFT_CS 15 
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);

const String url = "https://bseb.it/esp32/res";
DynamicJsonDocument doc(69797);
int currentResultIndex = 0;

String formatDate(long long timestamp) {
  time_t rawtime = timestamp / 1000;
  struct tm * ti;
  ti = localtime(&rawtime);
  
  char buffer[80];
  strftime(buffer, 80, "%d/%m/%Y %H:%M", ti);
  
  return String(buffer);
}

String getCourse() {
  long long startDate = doc["result"][currentResultIndex]["reservations"][0]["start_date"].as<long long>();
  String formattedDate = formatDate(startDate);
  String title = doc["result"][currentResultIndex]["reservations"][0]["title"].as<String>();
  String author_name = doc["result"][currentResultIndex]["reservations"][0]["teacher"]["name"].as<String>();
  String group_name = doc["result"][currentResultIndex]["reservations"][0]["student_group"]["group_name"].as<String>();
  String room_name = doc["result"][currentResultIndex]["reservations"][0]["rooms"][0]["name"].as<String>();
  
  String combinedInfo = "Cours du : " + formattedDate + "\nProf: " + author_name + "\nGroup: " + group_name + "\nTitle: " + title + "\nRoom: " + room_name;
  return combinedInfo;
}

void nextCourse() {
  if (doc.isNull()) {
    tft.setTextColor(ILI9341_WHITE);
    tft.println("\nLoading cours...");
    HTTPClient http;
    http.useHTTP10(true);
    http.begin(url);
    http.GET();
    WiFiClient *stream = http.getStreamPtr();
    DeserializationError error = deserializeJson(doc, *stream);
    http.end();
    if (error) {
      tft.setTextColor(ILI9341_RED);
      tft.println("\nError fetching data!");
      return;
    }
  }
  
  if (doc["result"][currentResultIndex].isNull()) {
    currentResultIndex = 0;
  }
  //clear screen
  tft.fillScreen(ILI9341_BLACK);
  
  tft.setTextColor(ILI9341_GREEN);
  tft.println(getCourse());
}

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);
  WiFi.begin(ssid, password, 6);
  tft.begin();
  tft.setRotation(1);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(2);
  tft.print("Connecting to WiFi");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    tft.print(".");
  }
  
  tft.print("\nOK! IP=");
  tft.println(WiFi.localIP());
  nextCourse();
}

void loop() {
  if (digitalRead(BTN_PIN) == LOW) {
    tft.fillScreen(ILI9341_BLACK);
    tft.setCursor(0, 0);
    currentResultIndex++;
    nextCourse();
  }
  delay(100);
}

