from random import randint
from time import sleep, time
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True

GRID = 8

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BIRD_X = 1               
GRAVITY = 0.5              
FLAP_STRENGTH = -1.6       
MAX_FALL_SPEED = 2.5
TICK_INTERVAL = 0.2        
PIPE_SPAWN_TICKS = 6      
PIPE_GAP_SIZE = 3          


def make_pipe():
    """A pipe is just {'x': column, 'gap_start': top row of the opening}."""
    gap_start = randint(0, GRID - PIPE_GAP_SIZE)
    return {"x": GRID - 1, "gap_start": gap_start}


def draw(bird_y, pipes, flash=None):
    pixels = [BLACK] * (GRID * GRID)

    for pipe in pipes:
        x = pipe["x"]
        if not (0 <= x < GRID):
            continue
        for y in range(GRID):
            if pipe["gap_start"] <= y < pipe["gap_start"] + PIPE_GAP_SIZE:
                continue
            pixels[y * GRID + x] = GREEN

    bird_row = int(round(bird_y))
    bird_row = max(0, min(GRID - 1, bird_row))
    pixels[bird_row * GRID + BIRD_X] = YELLOW

    sense.set_pixels(pixels)


def flash_screen(color, times=3):
    for _ in range(times):
        sense.clear(color)
        sleep(0.15)
        sense.clear()
        sleep(0.15)


def check_collision(bird_y, pipes):
    if bird_y <= 0 or bird_y >= GRID - 1:
        return True  

    bird_row = int(round(bird_y))

    for pipe in pipes:
        if pipe["x"] == BIRD_X:
            in_gap = pipe["gap_start"] <= bird_row < pipe["gap_start"] + PIPE_GAP_SIZE
            if not in_gap:
                return True
    return False


def play_round():
    bird_y = GRID / 2
    velocity = 0.0
    pipes = [make_pipe()]
    score = 0
    ticks_since_spawn = 0

    draw(bird_y, pipes)

    while True:
        flapped = False
        for event in sense.stick.get_events():
            if event.action != "pressed":
                continue
            if event.direction == "middle":
                return "quit", score
            flapped = True

        if flapped:
            velocity = FLAP_STRENGTH
        else:
            velocity = min(velocity + GRAVITY, MAX_FALL_SPEED)

        bird_y += velocity * 0.3  

        for pipe in pipes:
            pipe["x"] -= 1

        still_on_screen = []
        for pipe in pipes:
            if pipe["x"] < 0:
                score += 1
            else:
                still_on_screen.append(pipe)
        pipes = still_on_screen

        ticks_since_spawn += 1
        if ticks_since_spawn >= PIPE_SPAWN_TICKS:
            pipes.append(make_pipe())
            ticks_since_spawn = 0

        if check_collision(bird_y, pipes):
            return "lost", score

        draw(bird_y, pipes)
        sleep(TICK_INTERVAL)


def show_score(score):
    sense.show_message(f"Score: {score}", text_colour=BLUE, scroll_speed=0.05)


def main():
    sense.show_message("Ready?", text_colour=YELLOW)
    sense.show_message("Press any direction to flap", text_colour=(255, 255, 255), scroll_speed=0.05)

    while True:
        result, score = play_round()

        if result == "quit":
            sense.clear()
            break

        flash_screen(RED)
        show_score(score)
        sleep(0.3)


main()