AngryBotsInAiWorld
==================

A game for experimenting with sensorimotor AI.


API:
Player 1:
http://localhost:1235/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True
[Imgur](http://i.imgur.com/4RkNGEE.png)

Player 2:
http://localhost:1236/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True
[Imgur](http://i.imgur.com/thy5JUh.png)

`move_x, move_y, look_x, and look_y`
Float between -1.0 and 1.0

`shoot and jump`
Boolean `True` or `False`

Examples:
[random_bot.py](https://github.com/aiworld/AngryBotsInAiWorld/blob/master/examples/random_bot.py)
[twirling_bot (web - coffeescript)](https://github.com/aiworld/AngryBotsInAiWorld/tree/master/examples/twirling_bot)
