from machine import Pin
import utime
import time

# Sign matrix
# Character layout as on the 4x4 keyboard
matrix = [
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"],
["*", "0", "#"]]


#row_pins = [
#Pin(15, Pin.OUT),
#Pin(0, Pin.OUT),
#Pin(16, Pin.OUT),
#Pin(14, Pin.OUT)]
rows = [23,22,3,21]
cols = [19,5,17]

row_pins = [
Pin(23, Pin.OUT),
Pin(22, Pin.OUT),
Pin(3, Pin.OUT),
Pin(21, Pin.OUT)]

column_pins = [
Pin(19, Pin.IN, Pin.PULL_UP),
Pin(5, Pin.IN, Pin.PULL_UP),
Pin(17, Pin.IN, Pin.PULL_UP),
]

# Column pins in ascending order, counting from left to right
# I think that using SDA and SCL pins is allowed, as long as it does not interfere with data transfer
#column_pins = [
#Pin(13, Pin.IN, Pin.PULL_UP),
#Pin(12, Pin.IN, Pin.PULL_UP),
##Pin(5, Pin.IN, Pin.PULL_UP),
#Pin(2, Pin.IN, Pin.PULL_UP),
#Pin(4, Pin.IN, Pin.PULL_UP)
#]


def set_pins():
    # Setting pins:
    # Rows (upper four on WEMOS [D5-D8]) as output
    # Columns (lower four on WEMOS [D1-D4]) as input
    # D0 as an LED pin for testing purposes
    
    # Row pins in ascending order, counting from top to bottom
    row_pins = [
    Pin(23, Pin.OUT),
    Pin(22, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(21, Pin.OUT)]
    
    # Column pins in ascending order, counting from left to right
    column_pins = [
    Pin(19, Pin.IN, Pin.PULL_UP),
    Pin(5, Pin.IN, Pin.PULL_UP),
    Pin(17, Pin.IN, Pin.PULL_UP)]



def read_key():
    
    key = ""
    
    # Just as a precaution
    set_all_rows(1)
    
    # Cycles power through all rows,
    # stops when detects voltage change
    # (when it detects 1 on any input pin)

    for y in range(0, len(row_pins)):
        
        row_pins[y].off()

        for x in range(0, len(column_pins)):
            if column_pins[x].value() == 0:
                key = matrix[y][x]
                break
                
        row_pins[y].on()
        
    return key


def get_key():
    while True:
        time.sleep_ms(10) 
        key = read_key()
        if key != '':
            print("Key: ",key)
            break
    return key

# Sets all row pins to a defined value
def set_all_rows(value):
    for row in row_pins:
        row.value(value)

# Waits until a key is pressed and then released, then returns it
# Should be more stable than read_key_pressed(), triggers only as fast, as user can press buttons
def read_key_unpressed():
    start_time = utime.mktime(utime.localtime())
    key = ""
    test = "Anything"


    while(test != "" or key == ""):
        if utime.mktime(utime.localtime()) - start_time > 1:
            return "?"
        
        test = read_key()
        if not test == "":
            key = test
    
    return key

