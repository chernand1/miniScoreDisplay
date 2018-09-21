from luma.core import cmdline, error
from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas
from subprocess import check_output
import urllib.request
from math import floor

#import msvcrt

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

        try:
            urllib.request.urlopen('http://www.google.com/')
        except:
            print("Error: No internet connection")
            print("Check available SSID and connect")
            for line in scanoutput.split():
                if line.startswith(b'ESSID'):
                    ssid = line.split(b'"')[1]
                    print (ssid)
            return 0

        return 1

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
        self.background = self.background.resize((96, 96), Image.ANTIALIAS) \
            .transform(self.device.size, Image.AFFINE, (1, 0, -5, 0, 1, 15), Image.BILINEAR) \
            .convert(self.device.mode)

        self.device.display(self.background.convert(self.device.mode))

    def display_graphic(self, filepath, graphname="color_bars", extension="png"):
        self.background = Image.open(filepath + "/" + graphname + "." + extension)
        self.device.display(self.background.convert(self.device.mode))

'''
    def display(self, image):
        self._last_image = image.copy()
        self.device.display(image)


    def savepoint(self):
        """
        Copies the last displayed image.
        """
        if self._last_image:
            self.savepoints.append(self._last_image)
            self._last_image = None
'''

'''class keyboard_input:

    def __init__(self):
        self.buffer = 'eof'
        self.is_kbhit = 0

    def key_pressed(self):
        self.is_kbhit = msvcrt.kbhit()
        return self.is_kbhit
'''