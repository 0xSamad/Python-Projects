# Pomodoro Timer

A simple desktop Pomodoro timer built with Python's Tkinter, following the classic Pomodoro Technique: 25-minute work sessions with short breaks, and a longer break after every 4 work sessions.

## Demo

![Demo](demo/demo.gif)

## Features

- Start and reset controls
- Automatic switching between work sessions, short breaks, and long breaks
- Visual checkmark tracker (✔️) showing completed work sessions
- Clean, minimal UI with a tomato icon

## How It Works

- **Work session:** configurable work duration (default set for quick testing)
- **Short break:** after each work session
- **Long break:** after every 4th work session (8th rep)
- A checkmark is added for each completed work/break cycle, so you can track your progress at a glance

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `tomato.png` image file in the project directory

## Running It

```bash
python pomodoro.py
```

## Project Structure

```
.
├── main.py
├── tomato.png
├── demo/
│   └── demo.gif
└── README.md
```

## Notes

Work, short break, and long break durations are set as constants (`WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`) at the top of the script — adjust these to fit your preferred schedule (the classic Pomodoro Technique uses 25/5/20).
