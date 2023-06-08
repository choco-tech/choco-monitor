import src.app as app
from machine import reset

try:
    app.init()
    app.run()
except:
    reset()
