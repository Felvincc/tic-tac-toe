import os

def draw(row):
    clearScreen()
    print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
    print("\nDraw\n")
    exit()

def clearScreen():
    os.system('cls')

def end(row):
    clearScreen()
    print("wow you won the game your so cool and handosopme")
    print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
    exit()

def subsetChecker(lesserList, greaterList):
    return set(lesserList).issubset(set(greaterList))

def winCondition(x_boardState,o_boardState): 

    winConditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    for conditions in winConditions:
        x = subsetChecker(conditions, x_boardState)
        if x == True:
            return True
        else:
           pass

    for conditions in winConditions:
        x = subsetChecker(conditions, o_boardState)
        if x == True:
            return True
        else:
           pass
           
    return False        
        
def boardstr():
    return['| ' for x in range(4)]

def createboard(): #creates the board

    row1 = boardstr()
    row2 = boardstr()
    row3 = boardstr()
    return[row1, row2, row3]

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
    
def update(turns, x_boardState, o_boardState, row, whos_turn): #update the board


    if whos_turn % 2 == 0:
        b = 'O'
    else:
        b = 'X'
    print("\n<=====>")
    print("\nTurns:" + str(turns))
    print("Whos Turn: "+str(b))

    turns = turns+1

    if turns >=0 and turns<=9:
        

        userInput = int(input("\nenter number:"))

        if userInput in x_boardState or userInput in o_boardState:
            clearScreen()
            print("invalid ")
            turns = turns -1

            print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))

            update(turns, x_boardState, o_boardState, row, whos_turn)

        else:   

            whos_turn = whos_turn + 1

            clearScreen()
            temp = selector(row[0], row[1], row[2], userInput, whos_turn)

            if whos_turn % 2 == 0:
                x_boardState.add(temp)
            else:
                o_boardState.add(temp)
         
            print()
            print("\n<=====>\n")
            print(''.join(row[0]) + "\n" +''.join(row[1]) + "\n" +''.join(row[2]))
            
            gameState = winCondition(x_boardState,o_boardState)
            if gameState == True:
                end(row)
            else:
                pass

            update(turns, x_boardState, o_boardState, row, whos_turn)


            clearScreen()

    elif turns > 9:
        draw(row)

    else:
        exit()
    return(turns,x_boardState, o_boardState, row)

def play():
    turns = 0
    x_boardState = set()
    o_boardState = set()
    row = createboard()
    whos_turn = 0
    update(turns, x_boardState, o_boardState, row, whos_turn)

play()


#PULL REQUEST 2



