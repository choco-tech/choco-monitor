from machine import Pin
from dht import DHT22

from src.config.enviroments import envs, fake_services

dht22_sensor = DHT22(Pin(envs['DHT22_PORT']))

def collect_data():
    if fake_services['FAKE_DHT22']:
        return _collect_fake_data()
    else:
        return _collect_real_data()  

def _collect_fake_data():
    celsius, humidity = (20, 60)
    return celsius, humidity

def _collect_real_data():
    dht22_sensor.measure()
    
    humidity = dht22_sensor.humidity()
    celsius = dht22_sensor.temperature()
    
    return celsius, humidity