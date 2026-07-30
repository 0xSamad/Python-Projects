# Automated Birthday Wisher

A Python program that checks `birthdays.csv` every time it runs. If today matches someone’s birthday, it selects a random letter template, replaces `[NAME]` with their name, and sends them a birthday email.

## Features

- Reads birthday data from a CSV file
- Checks whether today is a listed birthday
- Randomly chooses one of three letter templates
- Personalizes the letter with the recipient's name
- Sends the email through Gmail SMTP

## Project Structure

```text
Automated Birthday Wisher/
│
├── main.py
├── birthdays.csv
├── requirements.txt
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## Installation

Install Pandas:

```bash
pip install pandas
```

## Birthday CSV Format

Your `birthdays.csv` file should look like this:

```csv
name,email,year,month,day
Hassan,hassan@example.com,2002,8,17
Ali,ali@example.com,1999,11,5
```

## Configure Your Email

In `main.py`, add your Gmail address and a **Google App Password**:

```python
MY_EMAIL = "your_email@gmail.com"
MY_PASS = "your_google_app_password"
```

> `MY_PASS` is **not your normal Gmail password**. It must be a 16-character Google App Password created specifically for this project.

## How to Create a Google App Password

1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Turn on **2-Step Verification** if it is not already enabled.
3. Return to the Security page and open **App passwords**.
4. Sign in again if Google asks you to.
5. Enter a name such as `Python Birthday Wisher`.
6. Click **Create**.
7. Copy the 16-character password Google provides.
8. Paste it into `MY_PASS` in `main.py`.

Example:

```python
MY_EMAIL = "your_email@gmail.com"
MY_PASS = "abcd efgh ijkl mnop"
```

Do not upload your real email password or Google App Password to GitHub.

## Run the Project

```bash
python main.py
```

If a birthday matches today’s date, the program sends a personalized birthday email.

## Technologies Used

- Python
- Pandas
- `datetime`
- `smtplib`
- `random`
