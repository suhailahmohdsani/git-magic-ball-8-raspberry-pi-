from sense_hat import SenseHat
import time

sense = SenseHat()

sense.set_imu_config(
    compass_enabled=True,
    gyro_enabled=False,
    accel_enabled=False
)

font = {
    "0": ["111", "101", "101", "101", "111"],
    "1": ["010", "110", "010", "010", "111"],
    "2": ["111", "001", "111", "100", "111"],
    "3": ["111", "001", "111", "001", "111"],
    "4": ["101", "101", "111", "001", "001"],
    "5": ["111", "100", "111", "001", "111"],
    "6": ["111", "100", "111", "101", "111"],
    "7": ["111", "001", "001", "001", "001"],
    "8": ["111", "101", "111", "101", "111"],
    "9": ["111", "101", "111", "001", "111"],
}

def get_direction(degree):
    if degree >= 337.5 or degree < 22.5:
        return "N"
    elif degree < 67.5:
        return "NE"
    elif degree < 112.5:
        return "E"
    elif degree < 157.5:
        return "SE"
    elif degree < 202.5:
        return "S"
    elif degree < 247.5:
        return "SW"
    elif degree < 292.5:
        return "W"
    else:
        return "NW"

while True:
    degree = sense.get_compass()
    direction = get_direction(degree)

    sense.clear()

  
    sense.show_letter(direction[0])

    time.sleep(0.5)