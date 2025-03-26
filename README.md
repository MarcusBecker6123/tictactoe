This little Command-Line game is just practice for myself.
First i created a welcome message and printed it out with the symbols "~" for the length of the message.
After that i created the Variables for the Board, 9 variables starting with a, so a-i, could've done that with numbers too.
The main() function is calling the gitter() and the game() function.
gitter() is printing the structure of the board with the Variables as placeholders.
game() is initializing first player as 'O'.
After that, a loop is created which asks the player, where he wants to put his mark 'O'.
Then i made a try expect block for checking if the user is giving a valid input, if the position on the board is already taken or
the user is giving a wrong variable which exceeds a-i and asking again for a valid insert.
After giving a valid input, checks if the current_player has won.
check_win() is checking for combinations i have prewritten and looping through each combination. if each key from value of combination list
equals to the players mark, return True and asks the user for another game or quit.
else, change the Player, if it's X change to O and the opposite.
When user wants to restart game, reset() flushes the dictionary of global var.
After that i recreate the dict var with 9 variables starting from a to i.
repeat until quit.
