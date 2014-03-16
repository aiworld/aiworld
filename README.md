#####API

Send an action to receive an image from both eyes, i.e.:

_Player 1_<br>
`http://localhost:1235/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True`

<img src="http://i.imgur.com/4RkNGEE.png"/>

_Player 2_<br>
`http://localhost:1236/?shoot=False&move_x=0.42&move_y=-0.42&look_x=-0.42&look_y=0.42&jump=True`

<img src="http://i.imgur.com/thy5JUh.png"/>

**Parameters**

Name       | Action                    | Type                      
---------  | -------------------       | -------------------------- 
move_x     | Strafe                    | Float between -1.0 and 1.0 
move_y     | Move forward, backward    | Float between -1.0 and 1.0 
look_x     | Look left, right          | Float between -1.0 and 1.0 
look_y     | Look up, down             | Float between -1.0 and 1.0 
shoot      | :boom:                    | Boolean True or False      
jump       | Currently disabled        | Boolean True or False      

#####Examples:

[random_bot.py](https://github.com/aiworld/AngryBotsInAiWorld/blob/master/examples/random_bot.py)

[twirling_bot (web - coffeescript)](https://github.com/aiworld/AngryBotsInAiWorld/tree/master/examples/twirling_bot)

#####Download

OS       | 64 bit | 32 bit                      
-------- | ------ | ------
OSX | [AngryBotsInAiWorld_x64.app.zip](https://www.dropbox.com/s/6nlji9u81q0yjyf/AngryBotsInAiWorld_x64.app.zip) |  [AngryBotsInAiWorld_x86.app.zip](https://www.dropbox.com/s/um0cw1r1da8dqg8/AngryBotsInAiWorld_x86.app.zip)
Windows | [AngryBotsInAiWorld_x64.exe.zip](https://www.dropbox.com/s/3atnk5pvlao9m7w/AngryBotsInAiWorld_x64.exe.zip) |  [AngryBotsInAiWorld_x86.exe.zip](https://www.dropbox.com/s/f2fyoz3doql702a/AngryBotsInAiWorld_x86.exe.zip)
Linux | [AngryBotsInAiWorld_x64.linux.zip](https://www.dropbox.com/s/7eua5fob1sq4ht2/AngryBotsInAiWorld_x64.linux.zip) | [AngryBotsInAiWorld_x86.linux.zip](https://www.dropbox.com/s/5ufyr2r7ajf9c2s/AngryBotsInAiWorld_x86.linux.zip)

#####TODO
- Allow changing image sizes
- Renable jump after fixing rampant falling of random bot
- Turn off development mode in unity build

_Based off [Angry Bots](https://www.assetstore.unity3d.com/#/content/12175) demo game for [Unity3D](http://unity3d.com/unity)._
