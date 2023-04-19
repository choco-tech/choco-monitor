from secret import wifi, thingspeak

envs = {
    'THINGSPEAK_WRITE_API_KEY': thingspeak['WRITE_KEY'],
    'UPDATE_TIME_INTERVAL': 5000,
    'WIFI_SSID': wifi['SSID'],
    'WIFI_PASSWORD': wifi['PASSWORD'],

    'DHT11_PORT': 14
}
