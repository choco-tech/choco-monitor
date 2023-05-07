from src.config.enviroments import envs
from src.core.wifi import do_connect
from src.core.mqtt.thingspeak_service import run_thingspeak
from src.core.mqtt.firebase.firebase_service import run_firebase
from update import start_update

def init():
    do_connect(envs['WIFI_SSID'], envs['WIFI_PASSWORD'])
    start_update()

def run():
    mqtt_server = envs['MQTT_SERVER']
    
    if mqtt_server == 'thingspeak':
        run_thingspeak()
    elif mqtt_server == 'firebase':
        run_firebase()
    else:
        print('Servidor MQTT inválido.')
