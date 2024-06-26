from machine import reset
from urequests import post

from src.config.enviroments import envs
from src.core.dht22 import collect_data
from src.utils.date_utils import get_date

from time import ticks_ms, sleep, mktime

def __send_data(json, api_key):
    request = post(
        f'http://api.thingspeak.com/update?api_key={api_key}',
        json = json,
        headers = {'Content-Type': 'application/json'} 
    )  
    request.close()
    
    print('Enviado:', json)

def run_thingspeak():
    api_key = envs['THINGSPEAK_WRITE_API_KEY']
    time_interval = envs['UPDATE_TIME_INTERVAL']

    last_update = ticks_ms()
    
    while True:
        if ticks_ms() - last_update >= time_interval: 
            try:
                celsius, humidity = collect_data()
                
                created_at = get_date()
                json_readings = { 'field1': celsius, 'field2': humidity, 'field3': mktime(created_at)} 

                __send_data(json_readings, api_key)
                
                last_update = ticks_ms()
            except Exception as e:
                print(e)
                print('Ocorreu um erro, reiniciando...')
                reset()