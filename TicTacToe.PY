import random
import os

'''  WIN CONDITIONS =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        chooses randomly 1 of the 8 win conditions to attempt
            >attempt to complete win condition
                >if selected win condition is blocked
                    >look for next available win conditions
                        >return
        scan for opponent win conditions
            >if sees opponent win condition
                >drop everything and block
                    >return
    '''

class game_structure:
    
    def winCondition(x_boardState,o_boardState): 

        winConditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

        for conditions in winConditions:
            x = util.subsetChecker(conditions, x_boardState)
            if x == True:
                return True
            else:
                pass

        for conditions in winConditions:
            x = util.subsetChecker(conditions, o_boardState)
            if x == True:
                return True
            else:
                pass
            
        return False        

    def update(turns, x_boardState, o_boardState, row, whos_turn, ai): #update the board

        

        if whos_turn % 2 == 0:
            b = 'X'
        else:
            b = 'O'
        #print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
        print("\n<=====>")
        print("\nTurns:" + str(turns))
        print("Whos Turn: " + str(b))

    

        turns = turns+1

        if turns >=0 and turns<=9:
            

            userInput = int(input("\nenter number:"))

            if userInput in x_boardState or userInput in o_boardState:
                util.clearScreen()
                print("invalid ")
                turns = turns -1

                print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))

                game_structure.update(turns, x_boardState, o_boardState, row, whos_turn, ai,)

            else:   

                whos_turn = whos_turn + 1

                util.clearScreen()
                temp = game_structure.selector(row[0], row[1], row[2], userInput, whos_turn)

                if whos_turn % 2 == 0:
                    x_boardState.add(temp)
                else:
                    o_boardState.add(temp)
            
                print()
                print("\n<=====>\n")
                print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
                
                gameState = game_structure.winCondition(x_boardState,o_boardState)
                if gameState == True:
                    ui.end(row)
                else:
                    pass

                game_structure.update(turns, x_boardState, o_boardState, row, whos_turn, ai,)


                util.clearScreen()

        elif turns > 9:
            ui.draw(row)

        else:
            exit()
        return(turns,x_boardState, o_boardState, row)

    def selector(row1,row2,row3,a,whos_turn): #selects which segment of the board to add the x thing
        
        if whos_turn % 2 == 0:
            b = 'O'
        else:
            b = 'X'

        if a>0 and a<4:
            row1[a - 1] = '|'+b
        elif a>2 and a<7:
            row2[a - 4] = '|'+b
        elif a>5 and a<10:
            row3[a - 7] = '|'+b
        else:
            print("invalid input BITCH!!!")
        return(a)

    def ai(x_boardState,o_boardState, avatar):
            win_conditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

            if avatar:
                ai=x_boardState
                player=o_boardState

            else:
                ai=o_boardState
                player=x_boardState

            #x = random.randint(0,7)
            x = 0

            print(win_conditions[x])
            print(player)
            is_present = any(item in player for item in win_conditions[x])

            if is_present:
                pass #next win condition
            else:
                print(is_present)

class ui:

    def start_menu():
        print("\ntic tac toe by jmdy\n\n")
        print("1: Pass and play")
        print("2. Play against AI")

        userInput = int(input("\n"))
        util.clearScreen()
        if userInput == 1:
            ai = False
            ui.play(ai)
        elif userInput == 2:
            ai = True
            ui.play(ai)
        else:
            ui.start_menu()

            print("sex")

    def draw(row):
        util.clearScreen()
        print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
        print("\nDraw\n")
        exit()

    def end(row):
        util.clearScreen()
        print("wow you won the game your so cool and handosopme")
        print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
        exit()

    def play(ai):
        turns = 0
        x_boardState = set()
        o_boardState = set()
        row = util.createboard()
        whos_turn=0
        userInput=None

        if ai:
            print("Which side would you like to play?") #avatar... i guess?
            print("1: X")
            print("2: O")
            userInput = int(input(""))
            util.clearScreen()
        else:

            if userInput == 2:

                whos_turn=1

            elif userInput == 1:

                whos_turn=0
                
            else:

                ui.play(ai)

        
        game_structure.update(turns, x_boardState, o_boardState, row, whos_turn, ai)

class util:
 
    def clearScreen():
        os.system('cls')

    def subsetChecker(lesserList, greaterList):
        return set(lesserList).issubset(set(greaterList))
    
    def boardstr():
        return['| ' for x in range(4)]

    def createboard(): #creates the board

        row1 = util.boardstr()
        row2 = util.boardstr()
        row3 = util.boardstr()
        return[row1, row2, row3]



ui.start_menu()






