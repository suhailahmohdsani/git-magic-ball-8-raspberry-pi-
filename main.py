from random import choice
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message('Ask Me A Question Bootiful', text_colour=(255, 0, 255), scroll_speed=0.01)
sleep(3)

replies = [('i dunno abt that...', (255, 255, 0)), ('YES! CONFORM', (0, 255, 0)), ('yu yao disagree lmao', (255, 0, 0))]

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2:
        reply, colour = choice(replies)
        sense.show_message(reply, text_colour=colour, scroll_speed=0.01)
    else:
        sense.clear()
