from miniDisplayScore import displayScore
from tm1637 import TM1637
import time
from fetchScores import football

matchToWatch = football(league='nfl')
matchToWatch.readHtmlFile()

display1 = displayScore()
display2 = displayScore()

display1.createDevice(portNo='0', bgcolor="red", reset_pin='25', rotate_screen=180)
display2.createDevice(portNo='1', bgcolor="green", reset_pin='22', rotate_screen=180)

display1.clearscreen(color="red")
time.sleep(2)



display2.clearscreen(color="green")
time.sleep(2)

'''
availablefonts = display1.fonttype()
print (availablefonts['1'])

'''

lcddisplay = TM1637(4, 21)

display1.check_wifi_network()
matchNumber = str(matchToWatch.getMatchNumber("Baltimore"))

while(1):
    lcddisplay.show_clock()
    if (matchToWatch.readHtmlFile("Baltimore") == True):
        display1.print_characters("Score!!!", "FreePixel", 30, 0, 0)
        time.sleep(2)

    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['team1'], "FreePixel", 30, 0, 0, "Red", 1)
    display1.print_characters(str(matchToWatch.getMatchDetail(matchNumber)['score1']), "FreePixel", 60, 20, 20, "Red", 1)

    display2.print_characters(matchToWatch.getMatchDetail(matchNumber)['team2'], "FreePixel", 30, 0, 0, "Blue", 1)
    display2.print_characters(str(matchToWatch.getMatchDetail(matchNumber)['score2']), "FreePixel", 60, 20, 20, "Blue", 1)

    time.sleep(2)
    lcddisplay.show_clock()
    display1.clearscreen("Black")
    display2.clearscreen("Black")
    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['timeleft'], "FreePixel", 60, 0, 0, "White")
    display2.print_characters(matchToWatch.getMatchDetail(matchNumber)['separator'], "FreePixel", 60, 0, 0, "White")
    time.sleep(2)
    display1.clearscreen("Black")
    display2.clearscreen("Black")
