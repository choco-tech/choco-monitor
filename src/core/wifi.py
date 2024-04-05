from network import WLAN, STA_IF
from time import sleep
from src.config.enviroments import envs

def do_connect(ssid, key):
    print(f'Tentando conectar {ssid}')
     
    wlan = WLAN(STA_IF)
    wlan.active(False) 
    wlan.active(True)
    wlan.config(reconnects = 5) 
    
    if not wlan.isconnected():
        wlan.connect(ssid, key)
                
        while not wlan.isconnected():
            pass     
        
    ip, mascara, gateway, dns = wlan.ifconfig()
    print(f'network config: ip = {ip}, máscara = {mascara}, gateway = {gateway}, dns = {dns}')
    

def find_an_network():
    print(f'Buscando rede')
    wifi_list = envs['WIFI_LIST']
        
    do_connect(wifi_list[0]['SSID'], wifi_list[0]['PASSWORD'])
