# Flashcards Tutor

A simple and interactive Graphical User Interface (GUI) application built with Python's `tkinter` module. It helps users learn French vocabulary through digital flashcards that automatically flip to reveal the English translation.

## Demo

![Demo](demo/demo.gif)

## How It Works

1. Launch the application.
2. A random French word is displayed on the flashcard.
3. After **3 seconds**, the card automatically flips to reveal the English translation.
4. Click the **✓ (Known)** button if you know the word. The word will be removed from your learning list.
5. Click the **✗ (Unknown)** button if you don't know the word, and it will appear again in future sessions.

Your learning progress is automatically saved, allowing you to continue from where you left off.

## Tech Used

- Python
- `tkinter` (standard GUI library)
- `pandas`
- `random`

## Run It Locally

```bash
pip install pandas
python main.py
