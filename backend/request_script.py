
import requests
import json
import random
import schedule
import time


def login():
    url = 'http://127.0.0.1:8000/api/token/'
    data = {'username': 'admin', 'password': 'admin'}
    response = requests.post(url, json=data)
    tokens = response.json()
    return tokens['access']


def get_count(token):
    url = 'http://127.0.0.1:8000/api/meters/get/'
    header = {'Content-type': 'application/json',
              'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=header)
    return int(response.json()["count"])


def get_value(id, token):
    url = f'http://127.0.0.1:8000/api/meters/get/{id}'
    header = {'Content-type': 'application/json',
              'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=header)
    return int(response.json()["Last_recorded_reading"])


def Update(id, reading, token):
    url = f'http://127.0.0.1:8000/api/meters/update/{id}'
    data = {'Last_recorded_reading': str(reading)}
    header = {'Content-type': 'application/json',
              'Authorization': f'Bearer {token}'}
    json_data = json.dumps(data)
    response = requests.put(url, data=json_data, headers=header)
    if int(response.status_code) == 200:
        print(f"The meter id {id} has been updated")
    else:
        print(f"There has been an error")


def main():
    token = login()
    count = get_count(token)
    id = random.randint(1, count)
    last_value = get_value(id, token)
    newValue = last_value + random.randint(0, 100)
    Update(id, newValue, token)


if __name__ == '__main__':
    print("The script has started")
    duration = 1
    schedule.every(duration).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
