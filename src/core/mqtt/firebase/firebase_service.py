import src.core.mqtt.firebase.ufirebase as firebase

from src.config.enviroments import envs
from src.core.dht11 import collect_data
from src.utils.date_utils import get_current_timestamp
from secret import room_info

from time import ticks_ms, sleep

def __put_data(topic_name, data):
    firebase.put(
        topic_name,
        data, 
        bg=0, 
    )
    print(data)
    
def __add_data(topic_name, data):
    firebase.addto(
        topic_name,
        data, 
        bg=0, 
    )
    print(data)

def run_firebase():
    firebase.setURL(envs['FIREBASE_URL'])

    firebase.put(
        f'rooms/{room_info["id"]}', 
        room_info,
        bg=0
    )

    time_interval = envs['UPDATE_TIME_INTERVAL']

    last_update = ticks_ms()

    while True:
        if ticks_ms() - last_update >= time_interval: 
            try:
                celsius, humidity = collect_data()
                
                readings = { 
                    'celsius': celsius, 
                    'humidity': humidity,
                    'roomId': room_info['id'],
                    'roomName': room_info['name']
                }
                
                __add_data('readings/dht11', readings)
                
                last_update = ticks_ms()
            except Exception as e:
                error = f'erro: main function, description: {str(e)}, created_at: {get_current_timestamp()}'
                print(error)

                __add_data(f'errors/{room_info["id"]}', error)
                
                sleep(1)
