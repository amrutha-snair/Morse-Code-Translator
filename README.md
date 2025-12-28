# Morse Code Translator

A backend-focused Python tool that translates text to Morse code and vice versa, and plays Morse audio.  
This project demonstrates text-to-signal encoding and core logic for communication systems.

---

## ✨ Features

- Translate English text → Morse code  
- Translate Morse code → English text  
- Play Morse code as audio signals  
- Modular design for future extensions

---

## 🧠 How It Works

Morse code is represented with:

- Dot: `.`
- Dash: `-`
- Letter separator: space (` `)
- Word separator: `/`

Audio playback uses timed sine-wave tones based on Morse timing rules.

---

## 📁 Project Structure

morse-project/
│
├── morse/
│ ├── init.py
│ ├── mappings.py # Morse dictionaries
│ ├── encoder.py # Text → Morse
│ ├── decoder.py # Morse → Text
│ ├── audio.py # Morse audio playback
│
├── main.py # CLI entry point
├── README.md
└── venv/ # Python virtual environment

---

## 🚀 Setup & Installation

1. Clone the repository:

git clone https://github.com/your-username/morse-project.git
cd morse-project

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install numpy simpleaudio

On Linux, you may need:

sudo apt install libasound2-dev

---

🛠 Usage

Run the main CLI interface:

python3 main.py

Choose one of the options:

Description

1	Convert text → Morse
2	Convert Morse → text
3	Play Morse as audio

---

🧪 Examples
Text → Morse

makefile

Input:  HELLO
Output: .... . .-.. .-.. ---
Play Morse Audio

makefile

Input: SOS
Audio: ... --- ...

---

🧩 Tech Stack

Python 3
NumPy
simpleaudio

---

⚠️ Limitations

WAV export not implemented yet

Fixed Morse speed

No real-time audio decoding

---

🚧 Future Improvements

WAV file export

Adjustable speed (words per minute)

GUI or web interface

Unit tests and CI/CD pipeline

---

📌 About

This project focuses on the fundamentals of encoding and decoding signals in software, illustrating how symbolic systems like Morse can be mapped to human-perceivable audio. It can serve as a foundation for more advanced DSP-oriented or communication-focused applications.

---








Sources
You said:
give descripti
