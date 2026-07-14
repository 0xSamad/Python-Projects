# Mail Merge Project

A simple Python script that generates personalized letters by merging a list of names into a template letter.

## Folder Structure

```
Mail Merge Project Start/
├── Input/
│   ├── Names/
│   │   └── invited_names.txt      # One name per line
│   └── Letters/
│       └── starting_letter.txt    # Template letter with [name] placeholder
├── Output/
│   └── ReadyToSend/                # Generated letters saved here
└── main.py
```

## How It Works

1. Reads all names from `invited_names.txt` (one name per line).
2. Reads the template from `starting_letter.txt`, which contains a placeholder `[name]`.
3. For each name, replaces `[name]` with the actual name.
4. Saves each personalized letter to `Output/ReadyToSend/` as `letter_for_<name>.txt`.

## Setup

1. Add names (one per line) to `Input/Names/invited_names.txt`.
2. Write your letter in `Input/Letters/starting_letter.txt`, using `[name]` wherever the recipient's name should appear.
3. Make sure the `Output/ReadyToSend/` folder exists (create it if it doesn't).

## Run

```bash
python main.py
```

- Names with trailing whitespace/newlines are automatically trimmed.
- The placeholder can be changed by editing the `PLACEHOLDER` variable in `main.py`.
- Output filenames are based on the name, so avoid characters in names that aren't valid in filenames (e.g. `/ \ : * ? " < > |`).
