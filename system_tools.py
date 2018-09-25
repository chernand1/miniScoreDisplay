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
        self.build_string = ''

    def get_key(self, isnumber):
        ch = os.read(sys.stdin.fileno(), 1)
        print(ch)
        if (isnumber == True) and (ch < b'\x30' or ch > b'\x39'):
            return '0'
        return ch.decode('utf-8')

    def get_string(self):
        for i in range (3):
            ch = os.read(sys.stdin.fileno(), 1)
            print(ch)
            if ch.decode != '':
                if self.build_string.find("\n") != -1:
                    self.build_string = ''
                else:
                    self.build_string = self.build_string + ch.decode('utf-8')
                    if ch.decode == '':
                        self.build_string = self.build_string + "\n"

        print("Len of string = " + str(len(self.build_string)))
        print("Position of back n" + str(self.build_string.find("\n")))

        #if (self.build_string[1] == "\n"):
        #    print("Found back slash n")
        #    self.build_string[2] = "\n"
        if (len(self.build_string) > 1) and (self.build_string.find("\n") != -1):
            print("Returned string" + self.build_string)
            return int(self.build_string)
        else:
            return 0
