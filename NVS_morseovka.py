morses = {'A': '.-', 'B': '-...', 'C': '-.-.',
          'D': '-..', 'E': '.', 'F': '..-.',
          'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..',
          'M': '--', 'N': '-.', 'O': '---',
          'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-',
          'V': '...-', 'W': '.--', 'X': '-..-',
          'Y': '-.--', 'Z': '--..', }


morse_s = {'.-' : 'A',      '-...': 'B',    '-.-.':'C',
          '-..' : 'D',     '.' : 'E',      '..-.':'F',
          '--.' : 'G',     '....': 'H',    '..':'I',
          '.---' : 'J',    '-.-': 'K',     '.-..':'L',
          '--' : 'M',      '-.': 'N',      '---': 'O',
          '.--.' : 'P',    '--.-': 'Q',    '.-.': 'R',
     	  '...' : 'S',     '-' : 'T',      '..-': 'U',
          '...-' : 'V',    '.--': 'W',     '-..-': 'X',
          '-.--' : 'Y',    '--..': 'Z',}

def morse():
    print()
    print("ŠIFROVÁNÍ MORSEOVY ABECEDY")
    print("     1.Zakódování")
    print("     2.Odkódování")
    print("Vyberte způsob šifrování: ")


    def encode():
        sentence = input("Co chcete zakódovat: ")
        print()
        for char in sentence:
          print(morses[char.upper()],end = " " )




    def decode():
        code = input ("Co chcete odkodóvat(mezi jednotlivými písmeny udělejte mezeru!!: ")
        print()
        for item in code.split(' '):
           print(morse_s.get(item), end = " " )

    def choices():
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
    retry = input("Chcete spustit program znovu ?(ano/ne)\n")
    if retry == "ano":
        print()
        morse()
    if retry == "ne":
        quit(0)



morse()