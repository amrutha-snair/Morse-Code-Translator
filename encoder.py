from morse.mappings import TEXT_TO_MORSE
def encode_text(text:str)->str:
    encoded_symbols=[]
    for char in text.upper():
        if char in TEXT_TO_MORSE:
            encoded_symbols.append(TEXT_TO_MORSE[char])
        else:
            continue
    return ''.join(encoded_symbols)