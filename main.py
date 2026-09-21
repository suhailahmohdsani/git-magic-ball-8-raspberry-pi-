from random import choice
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message('Ask Me A Question Bootiful')
sleep(3)

replies = ['i think so bro', 'i dunno abt that...', 'YES! CONFORM', 'HELL NAH!!!!', 'yu yao disagree lmao']

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        sense.show_message(choice(replies))
    else:
        sense.clear()



