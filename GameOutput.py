import machine
import ili9341
from xglcd_font import XglcdFont
from time import sleep
import math


import GameInput

class GameOutput:
    def __init__(self):
        #font_path = "/ArcadePix9x11.c"
        font_path  = "/Unispace12x24.c"
        spi = machine.SPI(1, baudrate= 1000000, miso=machine.Pin(19), mosi=machine.Pin(23), sck=machine.Pin(18))
        self.__display = ili9341.Display(spi, cs=machine.Pin(15),dc=machine.Pin(2),rst=machine.Pin(4), width=320, height=240, rotation = 270)
        self.__color_white = ili9341.color565(255,255,255)
        self.__font_obj = XglcdFont(font_path, 12, 24) #def __init__(self, path, width, height, start_letter=32, letter_count=96):
        
    
    # TEKST NIE JEST FORMATOWANY

    def print_screen(self, text):
        x = 0
        y = 0
        self.__display.clear()
        line_list = self.format_text(text)
        cntr = 0
        for line in line_list:
            self.__display.draw_text(x, y, line, self.__font_obj, self.__color_white)   #  def draw_text(self, x, y, text, font, color,  background=0, landscape=False, spacing=1):
            y += 30
            cntr += 1
            if cntr == 6:
                y +=30
                self.__display.draw_text(x, y, " [Przycisk] - czytaj dalej", self.__font_obj, self.__color_white) 
                y = 0
                cntr = 0
                sleep(3)

        
        print("\nTEXT PRINTED\n")
        sleep(10)                    
   
    def format_text(self,text):
        line_len = 26
        line_cnt = math.ceil(len(text)/line_len)
        line_list = []
        n = line_len
        m = 0
        for i in range(0, line_cnt):
            new_line = text[m:n]
            line_list.append(new_line)
            n += line_len
            m += line_len

        return line_list
