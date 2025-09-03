Classic Snake Game 🐍

A simple and classic implementation of the Snake game using Python's built-in turtle module. This project is a great demonstration of object-oriented programming principles in Python.

Features

  Classic Gameplay: Control a snake to eat food and grow longer.

  Score Tracking: Your score increases every time the snake eats a piece of food.

  Collision Detection: The game ends if the snake runs into the screen boundaries or its own body.

  Responsive Controls: Use the arrow keys to direct the snake's movement.
    
How to Play

Prerequisites

You just need to have Python 3 installed on your system. The turtle module comes standard with most Python installations, so no external libraries are needed.

Running the Game

  Save all the provided code into a single file named main.py.

  Open a terminal or command prompt.

  Navigate to the directory where you saved main.py.
  Run the main.py file
Controls

  Up Arrow: Move the snake up

  Down Arrow: Move the snake down

  Left Arrow: Move the snake left

  Right Arrow: Move the snake right

Objective: Eat the magenta food (●) to grow your snake and increase your score. Avoid hitting the walls or your own tail!

Code Structure

The program is structured into four main logical components, each handled by its own class.

   main.py (The main script): This file sets up the game screen, initializes all the game objects, and contains the main game loop that controls the flow of the game.

  Snake class: Manages all aspects of the snake, including creating its initial body, moving it forward, changing its direction, and extending it when it eats food.

  Food class: A subclass of Turtle that is responsible for placing the food at random locations on the screen.

  ScoreCard class: A subclass of Turtle used to display the current score on the screen and show the "GAME OVER" message when the game ends.
