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

    def get_key(self):
        ch = os.read(sys.stdin.fileno(), 1)
        return ch.decode('utf-8')

'''
init_anykey()
while True:
   key = anykey()
   if key != None:
      print key
   else:
      time.sleep(0.1)
'''
'''
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen. From http://code.activestate.com/recipes/134892/"""
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        self.impl = _GetchUnix()
        return self.impl


class _GetchUnix:
    def __init__(self):
        import tty, sys, termios # import termios now or else you'll get the Unix version on the Mac

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            print("Stuck before ch")
            ch = sys.stdin.read(1)
            print("Stuck after ch")
        finally:
            print("Finally ch")
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def getKey():
    print("Stuck before inkey")
    inkey = _Getch()
    print("Stuck after inkey")
    return inkey()
'''
'''
    import sys
    for i in xrange(sys.maxint):
        k=inkey()
        if k !='':break

    return k
'''