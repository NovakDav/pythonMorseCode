# \file NVS_morseovka.py
 # \brief Python soubor s komentáři
 #\author David Novák, Roman Juřík, Martin Miklík
 # \date Prosinec 2019
 # \details Konzolová aplikace - Překladač morseovy abecedy
 #   - Uživatel si může zvolit způsob překládání
 #      + z morseovy abecedy do čtivého jazyka
 #      + z čtivého jazyka do morseovky
 #   - Možnost znovuspuštění programu
 #
 # Zdrojové kódy jsou zapsány ve znakové sadě UTF-8




#\brief knihovna přiřazující k písmenům z abecedy znak z morseovy abecedy

morses = {'A': '.-', 'B': '-...', 'C': '-.-.',
          'D': '-..', 'E': '.', 'F': '..-.',
          'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..',
          'M': '--', 'N': '-.', 'O': '---',
          'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-',
          'V': '...-', 'W': '.--', 'X': '-..-',
          'Y': '-.--', 'Z': '--..','1':'1','2':'2',
          '3':'3','4':'4','5':'5','6':'6','7':'7',
          '8':'8','9':'9',' ': ' '}

#\brief knihovna přiřazující k znakům morseovy abecedy písmeno abecedy

morse_s = {'.-' : 'A',      '-...': 'B',    '-.-.':'C',
          '-..' : 'D',     '.' : 'E',      '..-.':'F',
          '--.' : 'G',     '....': 'H',    '..':'I',
          '.---' : 'J',    '-.-': 'K',     '.-..':'L',
          '--' : 'M',      '-.': 'N',      '---': 'O',
          '.--.' : 'P',    '--.-': 'Q',    '.-.': 'R',
     	  '...' : 'S',     '-' : 'T',      '..-': 'U',
          '...-' : 'V',    '.--': 'W',     '-..-': 'X',
          '-.--' : 'Y',    '--..': 'Z','1':'1','2':'2',
          '3':'3','4':'4','5':'5','6':'6','7':'7',
          '8':'8','9':'9',}


def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += morses[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher

def morse():

# !@brief funkce pro zakodování textu do morseovy abecedy
    def encode(sentence):
        print()
        # cyklus,který předělá textový řetězec do znaků
        for char in sentence:
             print(morses[char.upper()],end = " " )


# !@brief funkce pro změnu morseovy abecedy do čitelného textu
    def decode(code):
        print()
        #cyklus , který předělá znaky morseovy abecedy do abecedy
        for item in code.split(' '):
                print(morse_s.get(item), end = " " )




morse()