old_settings=None
import sys, tty, termios
import os, time

class get_char:

    def __init__(self):
        global old_settings
        old_settings = termios.tcgetattr(sys.stdin)
        new_settings = termios.tcgetattr(sys.stdin)
        new_settings[3] = new_settings[3] & ~(termios.ECHO | termios.ICANON) # lflags
        new_settings[6][termios.VMIN] = 0  # cc
        new_settings[6][termios.VTIME] = 0 # cc
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

    def get_key(self, isnumber, delay):
        ch = os.read(sys.stdin.fileno(), 1)
        print(ch)
        if (isnumber == True) and (ch < b'\x30' or ch > b'\x39'):
            return '0'
        return ch.decode('utf-8')
