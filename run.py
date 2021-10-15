import eel
from Banana import banana
from Hairbrush import brush
from Bottle import bottle


eel.init('web')

@eel.expose
def a():
    banana()

@eel.expose
def b():
    brush()

@eel.expose
def c():
    bottle()

eel.start('index.html', size=(1000, 600))
