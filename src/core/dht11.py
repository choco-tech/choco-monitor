from machine import Pin
from dht import DHT11

from src.config.enviroments import envs, fake_services

dht11_sensor = DHT11(Pin(envs['DHT11_PORT']))

def collect_data():
    if fake_services['FAKE_DHT']:
        return _collect_fake_data()
    else:
        return _collect_real_data()  

def _collect_fake_data():
    celsius, humidity = (20, 60)
    return celsius, humidity

def _collect_real_data():
    dht11_sensor.measure()
    
    humidity = dht11_sensor.humidity()
    celsius = dht11_sensor.temperature()
    
    return celsius, humidity