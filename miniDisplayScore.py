from luma.core import cmdline, error
from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas
from subprocess import check_output
import urllib.request
from math import floor
import time

class displayScore:

    rotate_conversion = {0: '0', 90: '1', 180: '2', 270: '3'}
    fontsdir = "fonts/"

    def __init__(self):
        self.resolutionX = 96
        self.resolutionY = 64
        self.type ='luma'
        self.chip = 'ssd1331'
        self.bus = 'i2c'
        self.portNumber = '0'

    def createDevice(self, type='luma', chip='ssd1331', width='96', height='64',bus='spi', portNo='0', bgcolor="black", reset_pin='25', rotate_screen='2'):

        self.resolutionX = width
        self.resolutionY = height
        self.type = type
        self.chip = chip
        self.bus = bus
        self.portNumber = portNo

        if type == 'luma':
            try:
                args = ('-d' + chip, '--width=' + width, '--height=' + height, '-i' + bus,
                        '--spi-device= '+ portNo, '--gpio-reset='+ reset_pin, '--rotate='+ self.rotate_conversion[rotate_screen])
                parser = cmdline.create_parser(description='luma.examples arguments')
                args1 = parser.parse_args(args)
                self.device = cmdline.create_device(args1)
                self.image = ImageDraw.Draw
                self.background = Image.new("RGBA", self.device.size, "Black")
                return 0
            except error.Error as e:
                return e

    def clearscreen(self, color="white"):

        self.background = Image.new("RGBA", self.device.size, color)
        #self.device.display(background.convert(self.device.mode))
        self.device.display(self.background.convert(self.device.mode))
        return 0

    def fonttype(self):
        return {'0': "code2000", '1': "FreePixel", '2': "pixelmix"}

    def print_characters(self, text, font, fontsize, posx=0, posy=0, color="White", autosize=1):

        if autosize == 1:
            fontsize = self.auto_size_text(text, font, fontsize)

        makefont = ImageFont.truetype(self.fontsdir + font + ".ttf", fontsize)
        draw = ImageDraw.Draw(self.background)
        draw.text((posx, posy), text, font=makefont, fill=color)

        self.device.display(self.background.convert(self.device.mode))

    def auto_size_text(self, text, font, fontsize):

        makefont = ImageFont.truetype(self.fontsdir + font + ".ttf", fontsize)

        with canvas(self.device) as draw:
            w, h = draw.textsize(text, makefont)

        new_font_size_X = fontsize
        new_font_size_Y = fontsize

        if w > int(self.resolutionX):
            new_font_size_X = floor(fontsize * ((int(self.resolutionX) - 5) / w))
        if h > int(self.resolutionY):
            new_font_size_Y = floor(fontsize * ((int(self.resolutionY) - 5) / h))

        if new_font_size_X > new_font_size_Y:
            return int(new_font_size_Y)
        else:
            return int(new_font_size_X)


    def check_wifi_network(self):

        scanoutput = check_output(["iwlist", "wlan0", "scan"])
        ssid = []
        try:
            urllib.request.urlopen('http://www.google.com/')
        except:
            print("Error: No internet connection")
            print("Check available SSID and connect")
            for line in scanoutput.split():
                if line.startswith(b'ESSID'):
                    ssid.append((line.split(b'"')[1]).decode('utf-8'))
                    print (ssid)
            return 1, ssid

        return 0, ''

    def download_and_display_graphic(self, urlbase, graphname="", extension="png"):

        try:
            url = urlbase + graphname + "." + extension
            graph_temp = urllib.request.urlopen(url)
            graph_data = graph_temp.read()
        except:
            print("Error: Unable to find " + graphname + "." + extension)
            print("url: " + url + " does not work")
            return -1

        img_path = "teamlogos/" + graphname + "." + extension
        f = open(img_path, "wb+")

        f.write(graph_data)

        self.background = Image.open(img_path)
        sizeX, sizeY = self.background.size

        # (1, 0, Translate X, 0, 1, Translate Y)
        self.background = self.background.resize((64, 64), Image.ANTIALIAS) \
            .transform(self.device.size, Image.AFFINE, (1, 0, -16, 0, 1, 0), Image.BILINEAR) \
            .convert(self.device.mode)

        '''
        self.background = self.background.resize((96, 96), Image.ANTIALIAS) \
            .transform(self.device.size, Image.AFFINE, (1, 0, -5, 0, 1, 15), Image.BILINEAR) \
            .convert(self.device.mode)
        '''
        self.device.display(self.background.convert(self.device.mode))

    def display_graphic(self, filepath, graphname="color_bars", extension="png"):
        self.background = Image.open(filepath + "/" + graphname + "." + extension)
        self.device.display(self.background.convert(self.device.mode))


    def return_array_index(self, input_array):
        print("i")
        number_of_screens = len(input_array)

        for i in range (number_of_screens):
            input_array.index()

    # Prints the list on the selected screen
    # and shows the current selection as color green
    def print_list_choice(self, display1, display2, headertext, listItems, currentSelection, font, fontsize, color="White", use_single=True):

        list_array = [[],[]]

        if use_single == True:
            display1 = self

        text_color = color
        #print("Header Text here...")
        #display1.print_characters(headertext, font, fontsize, 0, 0, text_color, 0)
        #time.sleep(5)
        number_line_feed = len(headertext.split("\n"))
        line_spaces = ""
        lines_per_screen = int(int(self.resolutionY) / fontsize)
        if (len(listItems) / lines_per_screen) > int(len(listItems) / lines_per_screen):
            number_of_screens = int(len(listItems) / lines_per_screen) + 1
        else:
            number_of_screens = int(len(listItems) / lines_per_screen)

        #print("Number of screens = " + str(number_of_screens))

        page_index = 0
        current_page_index = 0
        current_selection_index = 0

        for item in range(len(listItems)):

            if (item % 8 == 0) and (item != 0):
                page_index = page_index + 1
                list_array.append([])
                list_array.append([])

            if (item % 2 == 0):
                list_array[0 + 2* page_index].append(listItems[item])
                if item == currentSelection:
                    current_selection_index = len(list_array[0 + 2* page_index]) - 1
                    current_page_index = 2 * page_index
            else:
                list_array[1 + 2* page_index].append(listItems[item])
                if item == currentSelection:
                    current_selection_index = len(list_array[1 + 2* page_index]) - 1
                    current_page_index = 1 + 2 * page_index

        if (current_page_index % 2 == 0):
            page_to_display = current_page_index
        else:
            page_to_display = current_page_index - 1

        for i in range (len(list_array[page_to_display])):

            if (i == current_selection_index):
                print(list_array[current_page_index][current_selection_index])
                if (current_page_index % 2 == 0):
                    print("Screen 1 here --> Green here " + list_array[0][i])
                    print("Screen 2 here --> Normal " + list_array[1][i])
                else:
                    print("Screen 1 here --> Normal " + list_array[0][i])
                    print("Screen 2 here --> Green here " + list_array[1][i])
            else:
                print("To screen 1: " + list_array[page_to_display][i])
                if use_single == False:
                    print("To screen 2: " + list_array[page_to_display + 1][i])

        print("----")

        #print("Lines per screen = " + str(lines_per_screen))

        #print("Number line feed" + str(number_line_feed))
        #print(number_line_feed)

        for i in range(number_line_feed):
            line_spaces = line_spaces + "\n"
            #print("Is this used line space")

        #print("First Line spaces = " + str(line_spaces))

        lines_screen = 1

        string_screen1 = ""
        string_screen2 = ""


        for item in range (len(listItems)):

            if (item == currentSelection):
                text_color = "Green"
            else:
                text_color = color

            if use_single == True:
                #display1.print_characters(line_spaces + listItems[item] + "\n", font, fontsize, 0, 0, text_color, 0)
                display1.print_characters(listItems[item], font, fontsize, 0, (lines_screen - 1) * fontsize, text_color, 0)
                lines_screen = lines_screen + 1

            else:
                if (item % 2 == 0):
                    string_screen1 = string_screen1 + listItems[item] #+ "\n"
                    display1.print_characters(listItems[item], font, fontsize, 0, (lines_screen - 1) * fontsize, text_color, 0)

                else:
                    string_screen2 = string_screen2 + listItems[item] #+ "\n"
                    display2.print_characters(listItems[item], font, fontsize, 0, (lines_screen - 1) * fontsize, text_color, 0)
                    lines_screen = lines_screen + 1

            if ((lines_screen % (lines_per_screen + 1)) == 0) or (item == (len(listItems) - 1)):
                print("Inside if")
                #display1.print_characters(string_screen1, font, fontsize, 0, 0, text_color, 0)
                #display2.print_characters(string_screen2, font, fontsize, 0, 0, text_color, 0)
                string_screen1 = ""
                string_screen2 = ""
                lines_screen = 1
                time.sleep(2)
                display1.clearscreen("Black")
                if use_single == False:
                    display2.clearscreen("Black")
