# Spark

A Flask web app for encoding and decoding text using multiple techniques.

**Live demo:** [https://codez-9jsr.onrender.com/](https://codez-9jsr.onrender.com/)

## Techniques

| Technique   | Description |
|-------------|-------------|
| **Spark**   | Shifts each letter +6 positions in the alphabet, then reverses each word |
| **Reverse** | Reverses each word in the sentence |
| **Binary**  | Converts text to/from 8-bit binary representation |
| **Atbash**  | Substitutes each letter with its reverse-alphabet counterpart (a↔z, b↔y, etc.) |
| **Morse**   | Encodes/decodes text to/from Morse code |
| **Rail Fence** | Rail fence cipher using 3 rails |
| **ASCII**   | Shifts each character's ASCII value by +10 |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

The app starts at `http://0.0.0.0:8080`.

## Deploy

Built with Flask. Deploy on Render/Railway/Heroku using the included `Procfile`:

```
web: gunicorn app:app
```
