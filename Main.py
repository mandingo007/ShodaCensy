import os
from Censys import Censys_Main
from Shodan import Shodax


def Main():
    while True:
        os.system('cls')
        print """\n\n
                         /$$                                            
                        | $$                                            
 /$$  /$$  /$$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$ | $$ | $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$ | $$ | $$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
| $$ | $$ | $$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
|  $$$$$/$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
 \_____/\___/  \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/
            \n\n"""

        mode = int (raw_input("""
    [1] Censys.
    [2] Shodan.
    [3] Exit.
    ($)> """))
        if mode == 2:
            Shodax.Shodan_Mode()
        elif mode == 1:
            Censys_Main.Censys_Mode()
        elif mode == 3:
            sys.exit(1)
        else:
            print "[!] Invalid option please choose a valid one !"

if __name__ == '__main__':
    Main()