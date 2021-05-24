import machine
import ili9341
from xglcd_font import XglcdFont
from time import sleep


class GameOutput:
    def __init__(self):
        font_path = "/ArcadePix9x11.c"
        spi = machine.SPI(1, baudrate= 1000000, miso=machine.Pin(19), mosi=machine.Pin(23), sck=machine.Pin(18))
        self.__display = ili9341.Display(spi, cs=machine.Pin(15),dc=machine.Pin(2),rst=machine.Pin(4), width=320, height=240, rotation = 270)
        self.__color_white = ili9341.color565(255,255,255)
        self.__font_obj = XglcdFont(font_path, 9, 11) #def __init__(self, path, width, height, start_letter=32, letter_count=96):
        

    # TEKST NIE JEST FORMATOWANY
    def screen(self, text):
        self.__display.draw_text(100, 100, text, self.__font_obj, self.__color_white)   #  def draw_text(self, x, y, text, font, color,  background=0, landscape=False, spacing=1):
        print("\nTEXT PRINTED\n")
        sleep(10)                    
   


