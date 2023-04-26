from secret import wifi, thingspeak
from secret import sensors

envs = {
    'THINGSPEAK_WRITE_API_KEY': thingspeak['WRITE_KEY'],
    'UPDATE_TIME_INTERVAL': 5000,
    'WIFI_SSID': wifi['SSID'],
    'WIFI_PASSWORD': wifi['PASSWORD'],

    'DHT11_PORT': sensors['DHT11_PORT'],

    # firebase, thingspeak
    'MQTT_SERVER': 'thingspeak' 
}


fake_services = {
    'FAKE_DHT11': True,
}