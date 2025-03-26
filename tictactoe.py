import time
import sys
welcome_msg = "Willkommen zu Tic Tac Toe"
print(welcome_msg)


var = {chr(97+i):chr(97+i) for i in range(9)}                           #creates a dictionary with keys a-i and values a-i

def main():
    
    gitter()                                                            #prints the board   
    game()                                                              #starts the game

def reset():
    global var                                                          #makes var a global variable
    var.clear()                                                         #flushes the board(dictionary)
    var = {chr(97+i):chr(97+i) for i in range(9)}                       #sets dictionary to original a-i


def auswahl():
    choice = int(input("1. Spiel neustarten? \n2. Beenden ? \n"))       #asks user if they want to play again or exit
    if choice == 1:
        reset()                                                         #resets the board   

        main()
    elif choice == 2:
        sys.exit()                                                      #exits the game
    else:
        print("Keine gültige auswahl.")                                 #if user enters a number other than 1 or 2
        auswahl()                                                       

def game():
    
    current_player = 'O'                                                #player O starts the game
    
    while True:
        
        print(f"Spieler {current_player}, welches feld? (a-i): ")       #asks the player to choose a field
        
        wahl = input()                                                  #takes the input from the player
        
        try:                                                            #checks if the input is valid

            if var[wahl] == 'X' or var[wahl]=='O':                      #checks if the field is already taken
                print("Dieses feld ist schon besetzt")
                continue                                                #if the field is taken, the loop continues
            
            else:
                var[wahl] = current_player                              #if the field is not taken, the field is assigned to the current player
                time.sleep(1)
                gitter()

                if check_win(current_player) == True:                   #checks if the current player has won
                    print(f"Spieler {current_player} hat gewonnen.")    #prints the winner
                    auswahl()
                
                current_player = 'X' if current_player == 'O' else 'O'  #changes the player after each turn
        
        except KeyError:                                                #if the player enters a field other than a-i
            print("Bitte nur zwischen a-i auswählen")
            
    return

def check_win(current_player):
    
    win = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"],["a", "d", "g"],["b", "e", "f"], #all possible winning combinations
           ["c", "f", "i"],["a", "e", "i"],["c", "e", "g"]]
    
    for combination in win:                                             #checks if the current player has won
        
        if all(var[key] == current_player for key in combination):      #checks if all the fields in the combination are assigned to the current player
            
            return True
            
           
    return False

def gitter():                                                           #prints the board
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