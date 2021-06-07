from machine import Pin, ADC            
from time import sleep   
import machine               
import math
import ili9341
from xglcd_font import XglcdFont
import klawiatura



class GameInput:
    def __init__(self):
        spi = machine.SPI(1, baudrate= 1000000, miso=machine.Pin(19), mosi=machine.Pin(23), sck=machine.Pin(18))
        
        self.__display = ili9341.Display(spi, cs=machine.Pin(15),dc=machine.Pin(2),rst=machine.Pin(4), width=320, height=240, rotation = 270)
        self.__module_1 = ADC(Pin(32))
        self.__module_2 = ADC(Pin(35))

        self.__module_1.atten(ADC.ATTN_11DB)       #3.3V full range of voltage
        self.__module_2.atten(ADC.ATTN_11DB)



    def get_numpad(self):
        #returns string, see klawiatura.py
        key = klawiatura.get_key()
        return key

    def get_field(self):
        # CONSTS 
        square_num = 0
        err_margin = 0.15
        color = ili9341.color565(255,255,255)
        dict_of_values = { 4.63 : 1 , 3.67 : 2, 3 : 3, 2.47 : 4, 2 : 5, 1.56 : 6, 1.19 : 7, 0.87 : 8, 0.63 : 9, 5 : 10}
        # CONSTS END

        # FONT
        font_path  = "/Unispace12x24.c"
        unispace = XglcdFont(font_path, 12, 24) #def __init__(self, path, width, height, start_letter=32, letter_count=96):
        # FONT END

        self.__display.draw_text(100, 100, "Wprowadz pole", unispace, color)
        



        # GET VOLTAGE FROM ONE OF THE MODULES
        while True:

            time.sleep_ms(10)

            voltage_val_1 = self.__module_1.read() * 5 / 4095
            voltage_val_2 = self.__module_2.read() * 5 / 4095
            print("Voltage_val_1: ", voltage_val_1, "Voltage_val_2: ", voltage_val_2)

            if voltage_val_1 >= 0.1:
                voltage = voltage_val_1
                print("Voltage 1:  ", voltage)
                base = 0
                break
            if voltage_val_2 >= 0.1:
                voltage = voltage_val_2
                print("Voltage 1:  ", voltage)
                base = 10
                break


        # PICK SQUARE NUM ACCORDING TO VOLTAGE
        for key in dict_of_values:

            if abs(key - voltage) <= err_margin:
                square_num = dict_of_values[key]
                

        self.__display.draw_text(100, 100, "Pole odczytane", unispace, color)
        sleep(2)
        numer_pola = str(base + square_num)
        self.__display.draw_text(130, 130, numer_pola, unispace, color)
        sleep(3)
        
        return base + square_num








