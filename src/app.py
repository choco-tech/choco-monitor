from src.config.enviroments import envs
from src.core.wifi import find_an_network
from src.core.mqtt.firebase.firebase_service import run_firebase
from src.update import start_update

from src.utils.date_utils import set_ntp_time

def init():
    find_an_network()
    set_ntp_time()
    start_update()

def run():
    run_firebase()
    
