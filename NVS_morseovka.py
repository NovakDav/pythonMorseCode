"""
# \file NVS_morseovka.py
# \brief Python soubor s komentáři
# \author David Novák, Roman Juřík, Martin Miklík
# \date Listopad 2019
# \details Konzolová aplikace - Překladač morseovy abecedy
#   - Uživatel si může zvolit způsob překládání
#      + z morseovy abecedy do čtivého jazyka
#      + z čtivého jazyka do morseovky
#   - Možnost znovuspuštění programu
#
# Zdrojové kódy jsou zapsány ve znakové sadě UTF-8
"""

""" # \brief knihovna přiřazující k písmenům z abecedy znak z morseovy abecedy """

morses = {'A': '.-', 'B': '-...', 'C': '-.-.',
          'D': '-..', 'E': '.', 'F': '..-.',
          'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..',
          'M': '--', 'N': '-.', 'O': '---',
          'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-',
          'V': '...-', 'W': '.--', 'X': '-..-',
          'Y': '-.--', 'Z': '--..', '1': '1', '2': '2',
          '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
          '8': '8', '9': '9', ' ': ' '}

""" #\brief knihovna přiřazující k znakům morseovy abecedy písmeno abecedy """

morse_s = {'.-': 'A', '-...': 'B', '-.-.': 'C',
           '-..': 'D', '.': 'E', '..-.': 'F',
           '--.': 'G', '....': 'H', '..': 'I',
           '.---': 'J', '-.-': 'K', '.-..': 'L',
           '--': 'M', '-.': 'N', '---': 'O',
           '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U',
           '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', '1': '1', '2': '2',
           '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
           '8': '8', '9': '9', }


""" # !@brief založení funkce celého programu """
def morse():
    """ vypsání menu """
    print()
    print("ŠIFROVÁNÍ MORSEOVY ABECEDY")
    print("     1.Zakódování")
    print("     2.Odkódování")
    print("Vyberte způsob šifrování: ")

    # !@brief funkce pro zakodování textu do morseovy abecedy
    def encode():
        """ !@brief funkce pro zakodování textu do morseovy abecedy """
        # textový řetězec , který chceme zakodovat
        sentence = input("Co chcete zakódovat: ")
        print()
        # cyklus,který předělá textový řetězec do znaků
        for char in sentence:
            print(morses[char.upper()], end=" ")

    # !@brief funkce pro změnu morseovy abecedy do čitelného textu
    def decode():
        # zadání kodu , který chceme přeložit
        code = input("Co chcete odkodóvat(mezi jednotlivými písmeny udělejte mezeru!!: ")
        print()
        # cyklus , který předělá znaky morseovy abecedy do abecedy
        for item in code.split(' '):
            print(morse_s.get(item), end=" ")

    # !@brief funkce ,která v menu rozpozná jaký způsob kodovaní chceme vybrat
    def choices():
        # try/except ošetřuje chybové hlášky aby celý program nespadl a sputí program znovu
        try:
            choice = int(input())

            if choice == 1:
                encode()

            elif choice == 2:
                decode()
            else:
                print("špatná možnost, zkus to znovu")
                choices()
        except ValueError:
            print("špatná volba")
            morse()

    choices()

    print()
    print()
    # retry nám po ukončení kdoování nabídne spustit program znou nebo jej vypne
    retry = input("Chcete spustit program znovu ?(ano/ne)\n")
    if retry == "ano":
        print()
        morse()
    if retry == "ne":
        quit(0)


morse()
