#####API

Send an action to receive an image from both eyes.

_Player 1_<br>
`http://localhost:1235/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True`

<img src="http://i.imgur.com/4RkNGEE.png"/>

_Player 2_<br>
`http://localhost:1236/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True`

<img src="http://i.imgur.com/thy5JUh.png"/>

**Parameters**

Name      | Value
----------| -----
move_x    | Float between -1.0 and 1.0
move_y    | Float between -1.0 and 1.0
look_x    | Float between -1.0 and 1.0
look_y    | Float between -1.0 and 1.0
shoot     | Boolean True or False
jump      | Boolean True or False

####Examples:

[random_bot.py](https://github.com/aiworld/AngryBotsInAiWorld/blob/master/examples/random_bot.py)

[twirling_bot (web - coffeescript)](https://github.com/aiworld/AngryBotsInAiWorld/tree/master/examples/twirling_bot)

####TODO
- Allow changing image sizes
- Turn off development mode in unity build
- Renable jump after fixing rampant falling of the edge of world
