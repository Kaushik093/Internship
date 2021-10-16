import eel
import sys
import pyautogui
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

@eel.expose
def d():
    pyautogui.hotkey('ctrl', 'w')
    sys.exit()

eel.start('index.html', size=(1000, 600))
