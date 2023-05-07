import time
import ntptime

def set_ntp_time():
    try:
        print(time.localtime())
        ntptime.host = "a.ntp.br"
        
        ntptime.settime()
        print(time.localtime())
    except:
        print('Ocorreu um problema ao atualizar a data.')
        pass

def get_current_timestamp():
    ano, mes, dia, hora, min, seg, m, n = time.localtime(time.time())

    return f"{ano}/{mes}/{dia} {hora}:{min}:{seg}"
