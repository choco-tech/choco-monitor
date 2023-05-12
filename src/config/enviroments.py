from secret import wifi, thingspeak, firebase, room_info
from secret import sensors

envs = {
    'WIFI_SSID': wifi['SSID'],
    'WIFI_PASSWORD': wifi['PASSWORD'],

    # THINGSPEAK ENVS
    'THINGSPEAK_WRITE_API_KEY': thingspeak['WRITE_KEY'],
    
    # FIREBASE ENVS
    'FIREBASE_URL': firebase['URL'],

    # GENERAL ENVS
    'DHT11_PORT': sensors['DHT11_PORT'],

    'UPDATE_TIME_INTERVAL': 20000,

    # OPTIONS: firebase, thingspeak
    'MQTT_SERVER': 'firebase',

    'ROOM_ID': room_info['id']
}


fake_services = {
    'FAKE_DHT11': False,
}