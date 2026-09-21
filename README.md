# GiT Magic 8 Ball (Raspberry Pi) - Lai Yan & Suhailah

This project is a Magic 8 Ball that uses Raspberry Pi Sense HAT that gives a random response whenever it detects movement. Whenever there is movement detected, the LED lights would then display the premade responses and it would be randomised as well.

The 3 Responses Are:
  - 'i dunno abt that...' (Maybe - Yellow)
  - 'YES! CONFORM' (Yes - Green)
  - 'yu yao disagrees lmao' (No - Red)

How It Works:
  1. The Raspberry Pi displays **"Ask Me A Question Bootiful"** in purple
  2. The program waits for 3 seconds
  3. The Sense HAT continuously checks for movement
  4. If the Raspberry Pi is shaken, the program randomly chooses a response
  5. The response appears on the LED display in its assigned colour
  6. The program continues checking for movement until it is stopped
