
ChessEngine
ChessEngine is a chess AI implemented in Python. The engine uses the Minimax algorithm with Alpha-Beta pruning to determine the best move, providing an immersive and challenging game of chess.

Features
Adjustable AI depth: You can configure the depth of the AI's search algorithm, allowing you to choose the difficulty level of the AI.
Player vs. AI or AI vs. AI or Player vs. Player: Choose whether you want to challenge yourself against the AI or watch two AIs battle each other, or just play with yourself.

Getting Started
These instructions will guide you on how to deploy the project on your local machine for development and testing purposes.

Prerequisites
To run ChessEngine, you need to have Python and Pygame installed on your machine.

Python
If Python is not installed, you can download it from the official website:

Download Python
Download Pygame
After Python is installed, you can install Pygame using pip:
pip install pygame



Installation
Clone the ChessEngine repository to your local machine:

git clone https://github.com/Swoopi/Chess.git


Navigate into the cloned repository:

cd Chess
Now you can run the chess engine:


Configuration


Changing AI Depth
The AI's depth can be configured by changing the value of the DEPTH variable in the ChessAI.py file.

Example:

# Set the AI's depth to 4  (anything above that does not work) 
DEPTH = 4
Changing Game Mode
You can choose to play against the AI or have two AI opponents play against each other.

To play against the AI, playerOne represents White and playerTwo represents Black, if set to False, the Ai will play.

Example:
In ChessMain.py:

# Play against the AI
playerOne = True
playerTwo = False
White playing against BlackAI

Example:


# Two AIs play against each other
playerOne = False
playerTwo = False
White playing against BlackAI

#No AI play
playerOne = True
playerTwo = True


python ChessMain.py
This will start a game of chess. Enjoy!

Contributing
We welcome contributions to ChessEngine! Please see our Contributing Guide for more details.

Contact
If you have any questions or suggestions, feel free to reach out.

Please replace the URL in the git clone command with the URL of your actual repository. Also, create the CONTRIBUTING.md file to provide guidance on how to contribute to your project.
