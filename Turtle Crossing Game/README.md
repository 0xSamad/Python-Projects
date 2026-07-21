# Turtle Crossing Game

A fun, Frogger-style game built with Python's `turtle` module. Help the turtle cross a busy road without getting hit by the passing cars!

![Demo](demo/demo.gif)

## How It Works

1. The turtle starts at the bottom of the screen.
2. Use the **Up** arrow key to move the turtle forward.
3. Cars randomly generate on the right side of the screen and move left.
4. If you successfully reach the top of the screen (the finish line), you advance to the next level.
5. With each new level, the turtle returns to the start, and the cars move faster.
6. The game ends immediately if the turtle collides with any car.

## Tech Used

- Python
- `turtle` (standard library)
- `random` (standard library)
- `time` (standard library)

## Run It Locally

```bash
python main.py
```

No external dependencies required — just a standard Python installation.

## License

Feel free to use, modify, or build on this project.
