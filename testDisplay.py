from miniDisplayScore import displayScore
import time

display1 = displayScore()
display1.createDevice(portNo='1')

    # display1.clearscreen(color="red")
availablefonts = display1.fonttype()
print (availablefonts['1'])

display1.print_characters("This is a test", availablefonts['1'], 15)

while(1):
    time.sleep(1)