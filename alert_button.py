import time
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Someone pressed the alert button!"
    }
    requests.post(url, json=data)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_telegram_message()
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
