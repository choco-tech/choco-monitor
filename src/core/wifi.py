from network import WLAN, STA_IF

def do_connect(ssid, key):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
    
    ip, mascara, gateway, dns = wlan.ifconfig()
    print(f'network config: ip = {ip}, máscara = {mascara}, gateway = {gateway}, dns = {dns}')
