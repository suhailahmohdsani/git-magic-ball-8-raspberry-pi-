from sense_hat import SenseHat

sense = SenseHat()

sense.set_imu_config(
    compass_enabled=True,
    gyro_enabled=True,
    accel_enabled=False
)

while True:
    heading = sense.get_compass()

    if heading >= 337.5 or heading < 22.5:
        direction = 'N'
    elif heading < 67.5:
        direction = 'NE'
    elif heading < 112.5:
        direction = 'E'
    elif heading < 157.5:
        direction = 'SE'
    elif heading < 202.5:
        direction = 'S'
    elif heading < 247.5:
        direction = 'SW'
    elif heading < 292.5:
        direction = 'W'
    else:
        direction = 'NW'

    sense.show_message(f"{direction} {heading:.1f}")