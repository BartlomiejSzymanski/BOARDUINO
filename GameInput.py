from machine import Pin, ADC            
from time import sleep                  
import math



class GameInput:
    def __init__(self):

        self.__module_1 = ADC(Pin(32))
        self.__module_2 = ADC(Pin(35))
        self.__module_3 = ADC(Pin(39))
        self.__module_4 = ADC(Pin(36))

        self.__module_1.atten(ADC.ATTN_11DB)       #3.3V full range of voltage
        self.__module_2.atten(ADC.ATTN_11DB)
        self.__module_3.atten(ADC.ATTN_11DB)
        self.__module_4.atten(ADC.ATTN_11DB)


    def numpad(self):
        key = input('numpad: ')
        return key


    def get_coordinates(self):

        print("Wcisnij przycisk reprezentujacy plansze")
        
        module_list = [self.__module_1, self.__module_2, self.__module_3, self.__module_4]
        
        while True:
            for module_num in range(0,3):
                voltage_val = module_list[module_num].read() * 5 / 4095
                if voltage_val >= 0.2:
                    return module_num, voltage_val
                    
    def field(self):
        square_num = 0
        err_margin = 0.2
        #dict_of_values = { 0.4 : 1 , 0.8 : 2, 1.2 : 3, 1.6 : 4, 2 : 5, 2.4 : 6, 3 : 7, 3.4 : 8, 4 : 9, 4.4 : 10}
        dict_of_values = { 3.4 : 1 , 3.0 : 2, 4.8 : 3}
        module_num, voltage = self.get_coordinates()
        print(module_num, voltage)
        
        for key in dict_of_values:    

            if abs(key - voltage) <= err_margin:
                
                square_num = dict_of_values[key]
                print("Wartość klucza: ", key , "Wartość błędu: ", abs(key - voltage), "Square num: ", square_num)
        
        if module_num == 0:
            base = 0
        elif module_num == 1:
            base = 10
        elif module_num == 2:
            base = 20
        elif module_num == 3:
            base = 30
        
        return base + square_num

     

