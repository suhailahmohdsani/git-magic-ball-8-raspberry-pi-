from sense_hat import SenseHat
import random
import time

sense = SenseHat()

# Colours
snake_colour = [0, 255, 0]
food_colour = [255, 0, 0]
off = [0, 0, 0]

# Snake starts in the middle
snake = [(4, 4), (3, 4), (2, 4)]

# Direction: right
direction = (1, 0)

# Create food
def create_food():
    while True:
        food = (random.randint(0, 7), random.randint(0, 7))
        if food not in snake:
            return food

food = create_food()


def draw():
    sense.clear()

    # Draw snake
    for x, y in snake:
        sense.set_pixel(x, y, snake_colour)

    # Draw food
    sense.set_pixel(food[0], food[1], food_colour)


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

    # Move snake
    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)

    # Check wall collision
    if not (0 <= new_head[0] <= 7 and 0 <= new_head[1] <= 7):
        break

    # Check itself
    if new_head in snake:
        break

    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        food = create_food()
    else:
        snake.pop()

    draw()

    time.sleep(0.3)


# Game over
sense.clear()
sense.show_letter("X")

time.sleep(2)
sense.clear()