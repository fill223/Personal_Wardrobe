import time
import os

# тест на открытие всех ячеек
def all_cells_open():

    for i in range(49):
        os.system("gpio write " + i + " 1")
        time.sleep(2)
        os.system("gpio write " + i + " 0")

# Открытие ячейки cell на sec секунд
def cell_open(cell,sec):
    os.system("gpio write " + str(cell) + " 1") #Opening 
    print("Gpio №" + str(cell) + " was opened")
    time.sleep(sec)
    os.system("gpio write " + str(cell) + " 0") #Closing    
    print("Gpio №" + str(cell) + " was closed")   