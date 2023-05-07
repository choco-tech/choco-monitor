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

def authenticate():
    from src.core.mqtt.firebase.firebase_auth import FirebaseAuth

    auth = FirebaseAuth("AIzaSyClJO20-MbwmGtQacyQYb73h2Tx-tSHaxg")
    auth.sign_in('lucas.garcia15@fatec.sp.gov.br', 'ChocoFire')

def init():
    authenticate()

    firebase.setURL(envs['FIREBASE_URL'])

def run_firebase():
    init()

    firebase.put(
        f'rooms/{envs["ROOM_NAME"]}', 
        room_info,
        bg=0
    )

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
                    'created_at': created_at
                }
                
                __put_data(f'readings/dht11/{envs["ROOM_NAME"]}', readings)
                
                last_update = ticks_ms()
            except Exception as e:
                error = f"erro: main function, description: {str(e)}, created_at: {get_current_timestamp()}"
                print(error)

                __add_data(f'errors/{envs["ROOM_NAME"]}', error)
                
                sleep(1)
