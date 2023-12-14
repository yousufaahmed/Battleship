
# BATTLESHIP GAME

## Table of contents
* [Introduction](#Introduction)
* [Description](#Description)
* [Prerequisites](#Prerequisites)
* [Installation](#Installation)
* [Getting started](#Getting-started)
* [Testing](#Testing)
* [Details](#Details)

## Introduction

This is a Python implementation of the Battleship game, with a Flask UI. 

## Description

Players can place their ships on a board, and can play against an AI opponent (or multiplayer in a future iteration!), taking turns to sink eachothers ships until one or the other sinka all ships, declaring one side the winner!

There are 3 different versions of the game. One is a simple version, where you can attack ships on a predetermined board, giving coordinates in the terminal. The second is with an AI opponent, which can attack your board and you aim to destroy all the opponents ships before it destroys yours, which is also in the terminal. The third is the main game which can be played on the browser against the AI opponent.

## Prerequisites

To install Battleship, you will need to have python installed. Download python [here](https://www.python.org/downloads/)
* Python 3.7 or higher

## Installation

Flask is an external python library and so needs to be installed using pip.

1) Type cd followed by a space in the command prompt window
2) Drag and drop the battleship folder into the window and press Enter
3) Type in `pip install -U Flask` to download flask

For more information check out the official [flask](https://flask.palletsprojects.com/en/3.0.x/installation/) documentation: 

## Getting started

To play the Battleship game, follow these steps:

1) Type cd followed by a space in the command prompt window
2) Drag and drop the battleship folder into the window and press Enter

Windows:
```
$ cd C:\Users\user\Downloads\battleship
```
MacOS:
```
$ cd /Users/username/Downloads/battleship
```

3) Run the main application:
```
$ flask --app main run
```

4) Open your web browser and navigate to http://127.0.0.1:5000/placement
5) Click to place your battleships, with 'r' or 'R' to rotate the ships and start the game.

## Testing

All tests are present in a tests folder where each file contains the keyword "test". 

Pytest is an external python library and so needs to be installed using pip.
```
$ pip install pytest
```

You will also need to install these plugins:
```
$ pip install pytest-depends

```
```
$ pip install pytest-cov
```

To run the tests, use the following command:

### Windows:
```
$ python -m pytest 
```
### MacOS:
```
$ pytest
```
## Details

* **Authors:** Yousuf Ahmed [Linkedin](https://www.linkedin.com/in/yousufaahmed/)
* **License:** This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
* **Source:** [GitHub Repository](https://github.com/yousufaahmed/Battleship)