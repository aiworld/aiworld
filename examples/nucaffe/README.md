```
Bot controlled by caffe -> NuPIC sensorimotor loop.
                     ^_______|
```                     

* fais (First AI Shooter) is the Unity game project based off their AngryBots sample game.
* nupic_ contains the code and data used to train and run NuPIC via a cherrypy server.
* caffe_ contains the code and data for the pretrained nueral net that transforms images the bot sees into a series of features.

# Installation
* nupic_ and caffe_ use different versions of numpy so I recommend using virtualenv to separate their python environments.
* Otherwise for nupic_ install per https://github.com/numenta/nupic
* and caffe_ to http://caffe.berkeleyvision.org/installation.html making sure to use MKL BLAS for 5x speedup over OpenBLAS and 2x boost over ATLAS.
* Unity is required to edit and run fais: https://unity3d.com/unity/download

# Running
1. Start fais Unity game
2. `cd examples/nucaffe/nupic_ && python experiment.py`
3. `cd examples/nucaffe/caffe_ && python caffe_liaison.py`

Note: fais.csv is the training data used in the 2014 Numenta Hackathon.
However, filter_successes.py has since changed to give a more accurate representation of success.
A result of the new algorithm is successes.csv.

The algorithm used in the hackathon keyed off one successful time step and
saved the experience that surrounded that success. The new algorithm takes
a longer sequence of time steps into account and averages the success of all
time steps in that experience by shots_landed / times_shot and only then saves
the sequence.

Files that were created/modified in AngryBots to change the game to FPS from third person,
create two cameras for each bot as eyes that converge on a central focus, and
embed event loop HTTP servers within each player to capture image input and
receive actions are as follows:

* `Assets/Scripts/HTTPServer.cs`
* `Assets/Scripts/SaveScreen.cs`
* `Assets/Scripts/SpawnPlayers.cs`
* `Assets/Standard Assets/Autofire.cs`
* `Assets/Standard Assets/Eye.cs`
* `Assets/Standard Assets/ConvergeEye.cs`
* `Assets/Standard Assets/Health.js`
* `Assets/Standard Assets/Trigger.js`
* `Assets/Standard Assets/Character Controllers/Sources/Scripts/MouseLook.cs`



