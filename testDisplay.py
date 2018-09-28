from miniDisplayScore import displayScore
from tm1637 import TM1637
import time
from fetchScores import football, hockey, baseball
from system_tools import get_char

myKey = get_char()
lcddisplay = TM1637(4, 21)
lcddisplay.show_clock()

display1 = displayScore()
display2 = displayScore()

display1.createDevice(portNo='0', bgcolor="red", reset_pin='25', rotate_screen=180)
display1.display_graphic("misc_images", "color_bars2")
display2.createDevice(portNo='1', bgcolor="green", reset_pin='22', rotate_screen=180)
display2.display_graphic("misc_images", "color_bars2")
time.sleep(2)
display1.clearscreen("Black")
display2.clearscreen("Black")



error, ssid = display1.check_wifi_network()
if error == 1:
    display1.display_graphic("misc_images", "Internet-Access-Error")
    string_to_print_ssid = "Available SSIDs:"
    for ssid_disp in ssid:
        string_to_print_ssid = string_to_print_ssid + ssid_disp + "\n"
    display2.print_characters(string_to_print_ssid, "FreePixel", 16, 0, 0, "White", 0)
    time.sleep(10)

display1.print_characters("Choose Sport\nLeague", "FreePixel", 16, 0, 0, "White", 0)
display2.print_characters("1: NFL\n2: NHL\n3: MLB", "FreePixel", 16, 0, 0, "White", 0)
time.sleep(10)
display1.clearscreen("Black")
display2.clearscreen("Black")
keyPressed = myKey.get_string()
tmp_leagues = football('nfl')
selected_league = 'nfl'

if keyPressed > 0 and keyPressed <= len(tmp_leagues.available_leagues):
    selected_league = tmp_leagues.available_leagues[keyPressed -1]
    print("Selected league = " + selected_league)
    display1.print_characters(selected_league + " Selected", "FreePixel", 16, 0, 0, "White", 0)

time.sleep(5)
display1.clearscreen("Black")
display2.clearscreen("Black")

if selected_league.find('nfl') != -1:
    matchToWatch = football(league=selected_league)
else:
    if selected_league.find('nhl') != -1:
        matchToWatch = hockey(league=selected_league)
    else:
        print("Why baseball")
        matchToWatch = baseball(league=selected_league)

matchToWatch.readHtmlFile()

matchups = matchToWatch.getMatchups()

string_to_print_screen1 = ''
string_to_print_screen2 = ''
nb_of_matchups = len(matchups)
selected_match = 0
matchNumber = 0
print("Number of matchups = " + str(nb_of_matchups))
nb_loops = 0

while(selected_match == 0):
    string_to_print_screen1 = ''
    string_to_print_screen2 = ''
    #if nb_loops > 0:
        #time.sleep(5)
    display1.clearscreen("Black")
    display2.clearscreen("Black")
    for i in range(0, nb_of_matchups):
        print("i = " + str(i))
        if (i % 8 == 0):
            string_to_print_screen1 = ''
            string_to_print_screen2 = ''
            if (i !=0 ):
                time.sleep(5)
            display1.clearscreen("Black")
            display2.clearscreen("Black")

        if (i % 2 == 0):
            string_to_print_screen1 = string_to_print_screen1 + str(i+1) + ":" + matchups[i] + "\n"
            print(str(i) + ":" + matchups[i])
        else:
            string_to_print_screen2 = string_to_print_screen2 + str(i+1) + ":" + matchups[i] + "\n"
            print(str(i) + ":" + matchups[i])

        print("Screen 1 = " + string_to_print_screen1)
        print("Screen 2 = " + string_to_print_screen2)
        display1.print_characters(string_to_print_screen1, "FreePixel", 16, 0, 0, "White", 0)
        display2.print_characters(string_to_print_screen2, "FreePixel", 16, 0, 0, "White", 0)


    nb_loops = nb_loops + 1
    print("Number of loops = " + str(nb_loops))

    if string_to_print_screen1 != '':
        time.sleep(5)

    keyPressed = myKey.get_string()
    if keyPressed > 0 and keyPressed <= nb_of_matchups:
        matchNumber = keyPressed
        print("Selected Match Number = " + str(matchNumber))
        break

    # Time out 10 loops. Esxit While
    if nb_loops == 10:
        matchNumber = 1
        break

time.sleep(5)
display1.clearscreen("Black")
display2.clearscreen("Black")

full_team1_name = matchToWatch.getMatchDetail(matchNumber)['team1']
full_team2_name = matchToWatch.getMatchDetail(matchNumber)['team2']
selected_team_to_watch = full_team1_name

abrev_team1 = matchToWatch.get_cities_abrev(full_team1_name)
abrev_team2 = matchToWatch.get_cities_abrev(full_team2_name)

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

    display1.download_and_display_graphic("http://a.espncdn.com/combiner/i?img=/i/teamlogos/" + matchToWatch.league + "/500/", abrev_team1, "png")
    display2.download_and_display_graphic("http://a.espncdn.com/combiner/i?img=/i/teamlogos/" + matchToWatch.league + "/500/", abrev_team2, "png")
    #display2.download_and_display_graphic("http://a.espncdn.com/i/teamlogos/" + matchToWatch.league + "/500/scoreboard/", abrev_team2, "png")
    time.sleep(4)
    display1.clearscreen("Black")
    display2.clearscreen("Black")

