from sense_hat import SenseHat
import random
import time

sense = SenseHat()

snake_colour = [0, 255, 0]
food_colour = [255, 0, 0]

direction = (1, 0)


def create_food(snake):
    while True:
        food = (random.randint(0, 7), random.randint(0, 7))
        if food not in snake:
            return food


def change_direction(event):
    global direction

    if event.action != "pressed":
        return

    if event.direction == "up" and direction != (0, 1):
        direction = (0, -1)

    elif event.direction == "down" and direction != (0, -1):
        direction = (0, 1)

    elif event.direction == "left" and direction != (1, 0):
        direction = (-1, 0)

    elif event.direction == "right" and direction != (-1, 0):
        direction = (1, 0)


sense.stick.direction_any = change_direction


while True:

    snake = [(4, 4), (3, 4), (2, 4)]
    direction = (1, 0)
    food = create_food(snake)

    game_over = False

    while not game_over:

        head_x, head_y = snake[0]
        dx, dy = direction

        new_head = (head_x + dx, head_y + dy)

        if not (0 <= new_head[0] <= 7 and 0 <= new_head[1] <= 7):
            game_over = True
            break

        if new_head in snake:
            game_over = True
            break

        snake.insert(0, new_head)

        if new_head == food:
            food = create_food(snake)
        else:
            snake.pop()

        sense.clear()

        for x, y in snake:
            sense.set_pixel(x, y, snake_colour)

        sense.set_pixel(food[0], food[1], food_colour)

        time.sleep(0.3)

    sense.show_letter("X")
    time.sleep(1)

    sense.clear()
    time.sleep(0.5)