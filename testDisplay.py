from miniDisplayScore import displayScore
from tm1637 import TM1637
import time
from fetchScores import football

matchToWatch = football(league='nfl')
matchToWatch.readHtmlFile()
'''
display1 = displayScore()
display1.createDevice(portNo='1', bgcolor="red")
#display1.clearscreen(color="red")
time.sleep(2)


availablefonts = display1.fonttype()
print (availablefonts['1'])

'''

lcddisplay = TM1637(4, 21)
t = time.localtime()

d0 = lcddisplay.digit_to_segment[t.tm_hour // 10] if t.tm_hour // 10 else 0
d1 = lcddisplay.digit_to_segment[t.tm_hour % 10]
d2 = lcddisplay.digit_to_segment[t.tm_min // 10]
d3 = lcddisplay.digit_to_segment[t.tm_min % 10]

lcddisplay.set_segments([d0, d1, d2, d3])

#for i in range(1, 10):
    #display1.print_characters(str(i) + ":" + "0", availablefonts['0'], 20, posy=i)
    #lcddisplay.brightness = i + 6
    #lcddisplay.set_segments([i, ((0x80 & (i << 7)) & 0x80) + d1, d2, d3])
    #lcddisplay.set_segments([0xff, 0xff, 0xff, 0xff])
    #print(i<<7)
    #time.sleep(0.1)

lcddisplay.print_numbers("12:34")
time.sleep(3)
lcddisplay.print_numbers("5678")
time.sleep(3)
lcddisplay.print_numbers("56::78")
'''

display1.check_wifi_network()
matchNumber = str(matchToWatch.getMatchNumber("Green Bay"))

while(1):
    if (matchToWatch.readHtmlFile("Green Bay") == True):
        display1.print_characters("Score!!!", "FreePixel", 30, 0, 0)
        time.sleep(2)

    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['team1'] + "\n" +
                              str(matchToWatch.getMatchDetail(matchNumber)['score1']), "FreePixel", 30, 0, 0)
    time.sleep(2)
    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['team2'] + "\n" +
                              str(matchToWatch.getMatchDetail(matchNumber)['score2']), "FreePixel", 30, 0, 0)
    time.sleep(2)
    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['separator'], "FreePixel", 60, 0, 0)
    time.sleep(2)
'''