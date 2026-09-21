##Magic 8 Ball (Raspberry Pi) - Lai Yan & Suhailah

This project is a Magic 8 Ball built using a Raspberry Pi and Sense HAT. It provides a random response whenever the Raspberry Pi detects movement or shaking.

When movement is detected, the Sense HAT's LED matrix displays one of three randomly selected responses. Each response is displayed in a different colour to represent its answer.

Responses:
  - "Maybe" — Yellow
  - "Yes" — Green
  - "yu yao disagrees lmao" — Red

How It Works
  - The Raspberry Pi displays "Ask Me A Question" in purple
  - The program waits for 3 seconds.
  - The Sense HAT continuously checks for movement.
  - When the Raspberry Pi is shaken, the program randomly selects one of the three responses.
  - The selected response is displayed on the LED matrix in its assigned colour.
  - The program continues checking for movement until it is stopped.

Technologies Used
  - Raspberry Pi
  - Sense HAT
  - Python
  - Sense HAT LED Matrix
  - Motion Detection
  - Random Response Generation
  - Project Purpose

The purpose of this project is to explore how the Raspberry Pi Sense HAT's motion sensors and LED matrix can be combined with Python to create an interactive and entertaining application.
