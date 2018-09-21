from miniDisplayScore import displayScore
from tm1637 import TM1637
import time
from fetchScores import football

matchToWatch = football(league='nfl')
matchToWatch.readHtmlFile()

display1 = displayScore()
display2 = displayScore()

display1.createDevice(portNo='0', bgcolor="red", reset_pin='25', rotate_screen=180)
display1.display_graphic("misc_images", "color_bars2")
display2.createDevice(portNo='1', bgcolor="green", reset_pin='22', rotate_screen=180)
display2.display_graphic("misc_images", "color_bars2")

'''
availablefonts = display1.fonttype()
print (availablefonts['1'])

'''

lcddisplay = TM1637(4, 21)

display1.check_wifi_network()

selected_team_to_watch = "NY Jets"

matchNumber = str(matchToWatch.getMatchNumber(selected_team_to_watch))
full_team1_name = matchToWatch.getMatchDetail(matchNumber)['team1']
full_team2_name = matchToWatch.getMatchDetail(matchNumber)['team2']
abrev_team1 = matchToWatch.get_cities_abrev(full_team1_name)
abrev_team2 = matchToWatch.get_cities_abrev(full_team2_name)
time.sleep(2)
display1.clearscreen("Black")
display2.clearscreen("Black")

if len(abrev_team1) == 0 or len(abrev_team2) == 0:
    print("Fatal Error exiting program")
    exit()

while(1):
    lcddisplay.show_clock()
    if (matchToWatch.readHtmlFile(selected_team_to_watch) == True):
        for loop in range(1, 4):
            display1.print_characters("SCORE", "FreePixel", 60, 0, 0, "White", 1)
            display2.print_characters("!!!!!", "FreePixel", 60, 0, 0, "White", 1)
            time.sleep(1)
            display1.clearscreen("White")
            display2.clearscreen("White")
            display1.print_characters("SCORE", "FreePixel", 60, 0, 0, "Black", 1)
            display2.print_characters("!!!!!", "FreePixel", 60, 0, 0, "Black", 1)
            time.sleep(1)
            display1.clearscreen("Black")
            display2.clearscreen("Black")


    display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['team1'], "FreePixel", 30, 0, 0, "Red", 1)
    display1.print_characters(str(matchToWatch.getMatchDetail(matchNumber)['score1']), "FreePixel", 60, 20, 20, "Red", 1)

    display2.print_characters(matchToWatch.getMatchDetail(matchNumber)['team2'], "FreePixel", 30, 0, 0, "Blue", 1)
    display2.print_characters(str(matchToWatch.getMatchDetail(matchNumber)['score2']), "FreePixel", 60, 20, 20, "Blue", 1)

    time.sleep(2)
    lcddisplay.show_clock()
    display1.clearscreen("Black")
    display2.clearscreen("Black")
    lcddisplay.show_clock()
    #display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['timeleft'], "FreePixel", 60, 0, 0, "White")
    if len(matchToWatch.getMatchDetail(matchNumber)['separator']) < 4:
        display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['separator'], "FreePixel", 60, 0, 0, "White")
        display2.print_characters(matchToWatch.get_sport_separator(), "FreePixel", 60, 0, 0, "White")
    else:
        display1.print_characters(matchToWatch.getMatchDetail(matchNumber)['separator'], "FreePixel", 60, 0, 0, "White")

    time.sleep(2)
    display1.clearscreen("Black")
    display2.clearscreen("Black")
    lcddisplay.show_clock()
    display1.download_and_display_graphic("http://a.espncdn.com/i/teamlogos/" + matchToWatch.league + "/500/scoreboard/", abrev_team1, "png")
    display2.download_and_display_graphic("http://a.espncdn.com/i/teamlogos/" + matchToWatch.league + "/500/scoreboard/", abrev_team2, "png")
    time.sleep(4)
    display1.clearscreen("Black")
    display2.clearscreen("Black")

