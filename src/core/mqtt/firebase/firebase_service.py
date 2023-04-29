import src.core.mqtt.firebase.ufirebase as firebase

from src.config.enviroments import envs
from src.core.dht11 import collect_data
from src.utils.date_utils import get_current_timestamp
from secret import room_info

from time import ticks_ms, sleep, mktime

def __send_data(data):
    firebase.addto("readings/dht11/room1", data, bg=0)
    print('Enviado:', data)

def run_firebase():
    firebase.setURL(envs['FIREBASE_URL'])

    firebase.put("rooms/room1", room_info, bg=0)
	
    time_interval = envs['UPDATE_TIME_INTERVAL']

    last_update = ticks_ms()

    while True:
        if ticks_ms() - last_update >= time_interval: 
            try:
                celsius, humidity = collect_data()
                
                created_at = get_current_timestamp()
                
                readings = { 
                    'celsius': celsius, 
                    'humidity': humidity, 
                    'created_at': mktime(created_at) 
                }

                __send_data(readings)
                
                last_update = ticks_ms()
            except Exception as e:
                print(e)
                print('Ocorreu um erro, tentando novamente...')
                sleep(1)