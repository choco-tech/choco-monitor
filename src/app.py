from time import ticks_ms

from src.config.enviroments import envs
from src.core.wifi import do_connect
from src.core.dht11 import collect_data
from src.core.mqtt_server import send_data
from update import start_update

def init():
	do_connect(envs['WIFI_SSID'], envs['WIFI_PASSWORD'])
	start_update()

def run():
	api_key = envs['THINGSPEAK_WRITE_API_KEY']
	time_interval = envs['UPDATE_TIME_INTERVAL']

	last_update = ticks_ms()

	while True:
		if ticks_ms() - last_update >= time_interval: 
			try:
				celsius, humidity = collect_data()
				json_readings = { 'field1': celsius, 'field2': humidity } 
				
				send_data(json_readings, api_key)
				
				last_update = ticks_ms()
			except:
				print('Ocorreu um erro, tentando novamente')