import time
import numpy as np 
import simpleaudio as sa 

DOT_DURATION=0.1
DASH_DURATION=DOT_DURATION*3
SYMBOL_GAP=DOT_DURATION
LETTER_GAP=DOT_DURATION*3
WORD_GAP=DOT_DURATION*7
FREQUENCY=700
SAMPLE_RATE=44100

def _play_tone(duration:float):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(2 * np.pi * FREQUENCY * t)

    audio = wave * (2**15 - 1) / np.max(np.abs(wave))
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()

def play_morse(morse_code: str):
    for symbol in morse_code:
        if symbol == '.':
            _play_tone(DOT_DURATION)
            time.sleep(SYMBOL_GAP)

        elif symbol == '-':
            _play_tone(DASH_DURATION)
            time.sleep(SYMBOL_GAP)

        elif symbol == ' ':
            time.sleep(LETTER_GAP)

        elif symbol == '/':
            time.sleep(WORD_GAP)