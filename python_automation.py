import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : 8369311306,
        'message' : 'Hey bro its Akash Gretting you Good Morning',
        'key' : 'textbelt'
        }
    )
    print(resp.json())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)