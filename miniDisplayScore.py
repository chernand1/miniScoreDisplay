from luma.core import cmdline, error
from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas
from luma.core.virtual import viewport

class displayScore:


    def __init__(self):
        self.resolutionX = 96
        self.resolutionY = 64
        self.type ='luma'
        self.chip = 'ssd1331'
        self.bus = 'i2c'
        self.portNumber = '0'

    def createDevice(self, type='luma', chip='ssd1331', width='96', height='64',bus='spi', portNo='0'):

        self.resolutionX = width
        self.resolutionY = height
        self.type = type
        self.chip = chip
        self.bus = bus
        self.portNumber = portNo

        if type == 'luma':
            try:
                args = ('-d' + chip, '--width=' + width, '--height=' + height, '-i' + bus, '--spi-device= '+ portNo)
                parser = cmdline.create_parser(description='luma.examples arguments')
                args1 = parser.parse_args(args)
                self.device = cmdline.create_device(args1)
                return 0
            except error.Error as e:
                return e

    def clearscreen(self, color="white"):

        background = Image.new("RGBA", self.device.size, color)
        self.device.display(background.convert(self.device.mode))
        return 0

    def fonttype(self):
        return {'0': "code2000", '1': "FreePixel", '2': "pixelmix"}

    def print_characters(self, text, font, fontsize):

        fontsdir = "fonts/"
        makefont = ImageFont.truetype(fontsdir + font + ".ttf", fontsize)
        # draw = ImageDraw.Draw(background)
        with canvas(self.device) as draw:
            w, h = draw.textsize(text, makefont)
            #draw.multiline_text(0, "Please do not adjust your set", fill="black", align="center", spacing=-1)

        # First measure the text size
        with canvas(self.device) as draw:
            w, h = draw.textsize(text, makefont)

        virtual = viewport(self.device, width=max(self.device.width, w), height=max(h, self.device.height))
        with canvas(virtual) as draw:
            draw.text((0, 0), text, font=makefont, fill="white")
