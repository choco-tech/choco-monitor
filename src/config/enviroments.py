from secret import wifi_list, thingspeak, firebase, room_info
from secret import sensors

envs = {
    'WIFI_LIST': wifi_list,

    # THINGSPEAK ENVS
    'THINGSPEAK_WRITE_API_KEY': thingspeak['WRITE_KEY'],
    
    # FIREBASE ENVS
    'FIREBASE_URL': firebase['URL'],

    # GENERAL ENVS
    'DHT22_PORT': sensors['DHT22_PORT'],

    'UPDATE_TIME_INTERVAL': 20000,

    # OPTIONS: firebase, thingspeak
    'MQTT_SERVER': 'firebase',

    'ROOM_ID': room_info['id']
}


fake_services = {
    'FAKE_DHT': False,
}