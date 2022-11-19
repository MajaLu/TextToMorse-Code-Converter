from termcolor import colored


ENG_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


MORSE_TO_ENG = {}
for key, value in ENG_TO_MORSE.items():
    MORSE_TO_ENG[value] = key


def eng_to_morse(message):
    morse = []
    for char in message:
        if char in ENG_TO_MORSE:
            morse.append(ENG_TO_MORSE[char])
    return " ".join(morse)


def morse_to_eng(message):
    message = message.split(" ")
    english = []
    for code in message:
        if code in MORSE_TO_ENG:
            english.append(MORSE_TO_ENG[code])
    return " ".join(english)


def main():
    while True:
          response = input("Morse to English (MORSE) or English to Morse (ENGLISH)? : ").upper()


          if response == "MORSE":
                print("Enter Morse code (with a space after each code): ")
                morse = input(" ")
                english = morse_to_eng(morse)
                print(colored(english, "blue"))
                print(colored("To quit: QUIT", "red"))

          elif response == "ENGLISH":
                print("Enter text: ")
                english = input(" ").upper()
                morse = eng_to_morse(english)
                print(colored(morse, "blue"))
                print(colored("To quit: QUIT", "red"))
          else:
                response == "QUIT"
                break


if __name__ == "__main__":
    main()
