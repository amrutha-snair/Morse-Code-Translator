from morse.encoder import encode_text
from morse.decoder import decode_text
from morse.audio import play_morse

def main():
    print("Morse code translator")
    print("1.Text->Morse")
    print("2.Morse->Text")
    print("3.Play Morse Audio")

    choice=input("choose an option").strip()
    if choice.startswith('1'):
        text=input("Enter text: ")
        morse=encode_text(text)
        print("Morse:",morse)
    elif choice.startswith('2'):
        morse=input("Enter Morse code: ")
        print("Text:",decode_morse(morse))
    elif choice.startswith('3'):
        text=input("Enter text to play as Morse: ")
        morse=encode_text(text)
        print("Playing:",morse)
        play_morse(morse)
    else:
        print("Invalid")
if __name__=='__main__':
    main()
