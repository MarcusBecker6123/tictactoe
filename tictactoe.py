import time
import sys
welcome_msg = "Willkommen zu Tic Tac Toe"
print(welcome_msg)


var = {chr(97+i):chr(97+i) for i in range(9)}

def main():
    
    gitter()
    game()

def reset():
    global var
    var.clear()                                                         #flushes the board(dictionary)
    var = {chr(97+i):chr(97+i) for i in range(9)}                       #sets dictionary to original a-i


def auswahl():
    choice = int(input("1. Spiel neustarten? \n2. Beenden ? \n"))
    if choice == 1:
        reset()

        main()
    elif choice == 2:
        sys.exit()
    else:
        print("Keine gültige auswahl.")
        auswahl()

def game():
    
    current_player = 'O'
    
    while True:
        
        print(f"Spieler {current_player}, welches feld? (a-i): ")
        
        wahl = input()
        
        try:

            if var[wahl] == 'X' or var[wahl]=='O':
                print("Dieses feld ist schon besetzt")
                continue
            
            else:
                var[wahl] = current_player
                time.sleep(1)
                gitter()

                if check_win(current_player) == True:
                    print(f"Spieler {current_player} hat gewonnen.")
                    auswahl()
                
                current_player = 'X' if current_player == 'O' else 'O'
        
        except KeyError:
            print("Bitte nur zwischen a-i auswählen")
            
    return

def check_win(current_player):
    
    win = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"],["a", "d", "g"],["b", "e", "f"],
           ["c", "f", "i"],["a", "e", "i"],["c", "e", "g"]]
    
    for combination in win:
        
        if all(var[key] == current_player for key in combination):
            
            return True
            
           
    return False

def gitter():
    print("~" * len(welcome_msg))
    print(" "*7, end="")
    print(f" {var['a']} | {var['b']} | {var['c']} ")
    print(" "*7, end="")
    print(f"---+---+---")
    print(" "*7, end="")
    print(f" {var['d']} | {var['e']} | {var['f']} ")
    print(" "*7, end="")
    print(f"---+---+---")
    print(" "*7, end="")
    print(f" {var['g']} | {var['h']} | {var['i']} ")
    print("~" * len(welcome_msg))

main()