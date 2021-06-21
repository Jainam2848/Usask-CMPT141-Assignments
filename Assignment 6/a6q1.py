import numpy as np

#creating empty board
board=np.array([[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']])

#opening file
file=open('tictactoe_log2.txt','r')

log_data=[]
results={}
scores=[]

#filling log_data with lines of file
for lines in file:
    l = lines.split()
    log_data.append(l)
file.close()
#print(log_data)

def win_or_tie(player_1,player_2):
    """
    Parameters : names of players
    The function will check for wins row_wise, column_wise and diagonal_wise and return 
    the name of winning player. If no win is found then function will return tie.
    
    """
    #wins in row
    if (board[0][0]=='x' and board[0][1]=='x' and board[0][2]=='x') or (board[1][0]=='x' and board[1][1]=='x' and board[1][2]=='x') or (board[2][0]=='x' and board[2][1]=='x' and board[2][2]=='x'):
        return player_1
    elif (board[0][0]=='o' and board[0][1]=='o' and board[0][2]=='o') or (board[1][0]=='o' and board[1][1]=='o' and board[1][2]=='o') or (board[2][0]=='o' and board[2][1]=='o' and board[2][2]=='o'):
        return player_2
    
    #wins in column
    elif (board[0][0]=='x' and board[1][0]=='x' and board[2][0]=='x') or (board[0][1]=='x' and board[1][1]=='x' and board[2][1]=='x') or (board[0][2]=='x' and board[1][2]=='x' and board[2][2]=='x'):
        return player_1
    elif (board[0][0]=='o' and board[1][0]=='o' and board[2][0]=='o') or (board[0][1]=='o' and board[1][1]=='o' and board[2][1]=='o') or (board[0][2]=='o' and board[1][2]=='o' and board[2][2]=='o'):
        return player_2
    
    #wins in diagonal
    elif (board[0][0]=='x'and board[1][1]=='x' and board[2][2]=='x') or (board[0][2]=='x'and board[1][1]=='x' and board[2][0]=='x'):
        return player_1
    elif (board[0][0]=='o'and board[1][1]=='o' and board[2][2]=='o') or (board[0][2]=='o'and board[1][1]=='o' and board[2][0]=='o'):
        return player_2
    else:
        return 'TIE'

def update_results(p_1,p_2,winner):
    """
    Parameters : p_1 and p_2, names of players
    It will check for the name of player in our dictionary of results,
    if the name is not found, it will create a record for those.
    If name is found, then it will update the record in dictionary with wins,losses and ties
    
    
    """
   
    if p_1 not in results:
        results[p_1]={'wins':0,'losses':0,'ties':0}
    if p_2 not in results:
        results[p_2]={'wins':0,'losses':0,'ties':0}
    if winner == p_1:
        results[p_1]['wins'] += 1
        results[p_2]['losses'] += 1
    elif winner == p_2:
        results[p_2]['wins'] += 1
        results[p_1]['losses'] += 1
    elif winner == 'TIE':
        results[p_1]['ties'] +=1
        results[p_2]['ties'] +=1


def update_scores():
    """
    Parameters : No parameters
    The function will calculate and update tournament scores of players in results
    
    """
    for player in results:
        results[player]['tournament score']=(results[player]['wins']-results[player]['losses'])/(results[player]['wins']+results[player]['losses']+results[player]['ties'])

def reset_board():
    """ Parameters : No parameters
        
        Purpose : The function will clear/clean the board after the game is played
        
        Return :  Function will return new board"""
    global board
    board=np.array([['','',''],
                ['','',''],
                ['','','']])
    return board
def new_game():
    """
    Parameter : No parameter
    
    The function will use data to run the game, it will search for "NEWGAME" to start a new game.
    after running the game, the function will check for win,lose or tie and will update to results
    to the dictionary. It will search for ENDGAME to finish the game, After the game is over, the
    game board will be reset for the new game.and the previous data of the game will be deleted.
    The function will run continuously till it finds "Done" in the log file.
      
    """
    p1=""
    p2=""
    if log_data[0][0]=='NEWGAME':
        p1=log_data[0][1]
        p2=log_data[0][2]
        del log_data[0]
        #making rows and columns
        while log_data[0][0]=='x' or log_data[0][0]=='o':
            rows=int(log_data[0][1])
            columns=int(log_data[0][2])
            
            #creating board of the game
            board[rows,columns]=log_data[0][0]
            del log_data[0]
            
    #ending the game, if word "ENDGAME" is found and then finding the winner or tie and updating scores
    #followed by resetting the board
    if log_data[0][0]=='ENDGAME':
        Winner= win_or_tie(p1,p2,)
        update_results(p1,p2,Winner)
        reset_board()
        del log_data[0]

while log_data[0][0] != 'DONE':
    new_game()

update_scores()

for player in list(results):
    print(player,':',results[player])
    scores.append(results[player]['tournament score'])

#Finding the maximum and minimum score
max_score=max(scores)
min_score=min(scores)

#Checking for player with highest score
for player in results:
    if results[player]['tournament score']==max_score:
        Highest_rank=player
        
#Checking for player with highest score
for player in results:
    if results[player]['tournament score']==min_score:
        Lowest_rank=player


print("The highest-ranked player is: ",Highest_rank)
print("The lowest-ranked player is: " ,Lowest_rank)