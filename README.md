# Asteroids Clone

This project is a clone of the classic game Asteroids, implemented using the pygame library. It is based on a lesson from Boot.dev.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/asteroids-clone.git
    cd asteroids-clone
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install pygame
    ```

## How to Play

1. Run the game:
    ```bash
    python main.py
    ```

2. Controls:
    - `WASD`: Move and rotate the player.
    - `Spacebar`: Fire shots.

3. Objective:
    - Shoot the asteroids to split them into smaller asteroids.
    - Avoid colliding with the asteroids.

## Code Structure

- `main.py`: Contains the main game loop and initializes the game.
- `player.py`: Defines the `Player` and `CircleShape` classes used to create and manage the player.
- `asteroid.py`: Defines the `Asteroid` class which handles the asteroid behavior, including splitting into smaller asteroids.
- `asteroidfield.py`: Manages a field of asteroids.
- `shot.py`: Defines the `Shot` class to handle the behavior of shots fired by the player.
- `constants.py`: Contains game constants like screen dimensions and asteroid properties.

## Contributions

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project was created as part of a lesson from [Boot.dev](https://boot.dev).