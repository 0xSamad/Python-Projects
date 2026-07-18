# US States Guessing Game

A fun little turtle-graphics game that tests how many US states you can name from memory.

<p align="center">
  <img src="demo/demo.mp4" alt="Demo" width="100%">
</p>

## How It Works
- A blank map of the US is displayed as the game background.
- Type a state name into the popup box, and if it's correct, the name appears on the map at its correct location.
- Keep guessing until you've named all 50 states, or type **Exit** to quit early.
- Any states you didn't guess are saved to `States_to_learn.csv` so you can study them later.

## Requirements
```
pip install pandas
```
(Turtle comes built-in with Python.)

## Files Needed
- `blank_states_img.gif` — the blank US map image
- `50_states.csv` — CSV with columns `state`, `x`, `y` (state name and its coordinates on the map)

## Run It
```bash
python main.py
```

## Output
- `States_to_learn.csv` — auto-generated list of states you missed, for review.

---
Good luck naming all 50! 🇺🇸

No external dependencies required — just a standard Python installation.

## License

Feel free to use, modify, or build on this project.




