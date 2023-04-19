from urequests import post

def send_data(json, api_key):
    request = post(
        f'http://api.thingspeak.com/update?api_key={api_key}',
        json = json,
        headers = {'Content-Type': 'application/json'} 
    )  
    request.close()
    
    print('Enviado:', json)
