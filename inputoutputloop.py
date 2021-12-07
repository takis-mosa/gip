# input/output loop
import sensor_driver
import scherm_driver

def lees_invoer():
    d = sensor_driver.read()
    return d

def schrijf_uitvoer(data):
    scherm_driver.schrijf(data)

while True:
    data = lees_invoer()
    schrijf_uitvoer(data)
