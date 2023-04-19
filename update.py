from machine import Pin, reset
import gc

from src.ota.ota_updater import OTAUpdater

update_led = Pin(2, Pin.OUT)

def check_for_updates():
    otaUpdater = OTAUpdater(
        'https://github.com/choco-tech/choco-monitor', 
        main_dir='src'
    )
    hasUpdated = otaUpdater.install_update_if_available()

    if hasUpdated:
        reset()
    else:
        del(otaUpdater)
        gc.collect()

def start_update():
    update_led.value(1)

    check_for_updates()

    update_led.value(0)