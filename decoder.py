from morse.mappings import MORSE_TO_TEXT
def decode_text(morse_code:str)->str:
    decoded_chars=[]
    symbols=morse_code.strip().split(' ')
    for symbol in symbols:
        if symbol=='/':
            decoded_chars.append(" ")
        elif symbol in MORSE_TO_TEXT:
            decoded_chars.append(MORSE_TO_TEXT[symbol])
        else:
            decoded_chars.append('?')
    return "".join(decoded_chars)
