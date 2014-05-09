from caffe import imagenet
import requests
from StringIO import StringIO
import numpy as np
from PIL import Image
import json
from datetime import datetime
from random import random

# Set the right path to your model file, pretrained model,
# and the image you would like to classify.
MODEL_FILE = 'imagenet/imagenet_deploy.prototxt'
PRETRAINED = 'imagenet/caffe_reference_imagenet_model'

PLAYER_HOST  = 'http://localhost:1236'
NUPIC_HOST   = 'http://localhost:8080'

net = imagenet.ImageNetClassifier(
    MODEL_FILE, PRETRAINED, center_only=1)

net.caffenet.set_phase_test()
net.caffenet.set_mode_cpu()


def perceive(action):
    r = requests.get(PLAYER_HOST, params=action)
    image = np.array(Image.open(StringIO(r.content)), dtype=None)
    return image


def predict(image, action):
    features = net.predict(image)
    r = requests.get(NUPIC_HOST, params={
        'f189': features[189],  # Picked by NuPIC swarm.
        'move_x': action['move_x']
    })
    action['move_x'] = float(r.content)
    return action


def record_game():
    """For recording a game against a random bot."""
    i = 0
    with open("fais.json" + str(datetime.now()), "a") as f:
        while True:
            payload = {
                'move_x' : random() * 2.0 - 1.0,
                'move_y' : random() * 2.0 - 1.0,
                'look_x' : random() * 2.0 - 1.0,
                'look_y' : random() * 2.0 - 1.0,
                'jump'   : random() < 0.5,
                'shoot'  : random() < 0.5
            }
            r = requests.get(PLAYER_HOST, params=payload)
            im = np.array(Image.open(StringIO(r.content)), dtype=None)
            f.write(json.dumps({
                'requestHeaders'  : payload,
                'responseHeaders' : dict(r.headers),
                'features'        : net.predict(im).tolist()
            }) + '\n')
            print str(i)
            i += 1


def play_game():
    action = {
        'move_x' : 0.0,
        'move_y' : 0.0,
        'look_x' : 0.0,
        'look_y' : 0.0,
        'jump'   : False,
        'shoot'  : True
    }
    while True:
        action = predict(image=perceive(action), action=action)

play_game()
