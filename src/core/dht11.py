from machine import Pin
from dht import DHT11

from src.config.enviroments import envs

dht11_sensor = DHT11(Pin(envs['DHT11_PORT']))

def collect_data():
    dht11_sensor.measure()
    
    humidity = dht11_sensor.humidity()
    celsius = dht11_sensor.temperature()
    
    return celsius, humidity
