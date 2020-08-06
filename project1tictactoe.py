def main():
    board=['#','','','','','','','','','']
    order=take_input()
    chance=1
    playgame(board,chance,order)    
def take_input():
    check=''
    while not (check=='x' or check=='o'):
        print("player 1 choose x or o:")
        marker=input()
        player1=marker
        check=player1
        if player1=="x":
            player2="o"
        else:
            player2="x"
    if player1=="x":
        return('x','o')
    else:
        return('o','x')   
def playgame(board,chance,order):
    pos=0
    marker=None
    while not isboardfull(board) and not checkwin(board):
        pos=0
        while pos not in range(1,10):
            if chance==1:
                print("player1 please enter position from 1-9")
                marker= order[0]
                chance=2
            else:
                print("player2 please enter your position")
                chance=1
                marker=order[1]
            pos=int(input())
            flag=updateboard(board,pos,marker)
            if flag==1:
                continue
            if flag==0:
                if chance==1:
                    chance=2
                else:
                    chance=1                   
    if checkwin(board):
        if chance==2:
            print("player1 won the match")
        elif chance==1:
            print("player 2 won the match")
    else:
        print("draw")     
def printboard(board):
    print(board[1]+ " |" +board[2]+ " |"+board[3])
    print("-"*5)
    print(board[4]+ " |" +board[5]+ " |"+board[6])
    print("-"*5)
    print(board[7]+ " |" +board[8]+ " |"+board[9])
    print("-"*5)
    return
def updateboard(board,pos,marker):
    if board[pos]=='':
        board[pos]=marker
        printboard(board)
        return 1
    else:
        print("invalid")
        return 0   
def isboardfull(board):
    for i in range(1,len(board)):
        if board[i]=='':
            return False
    return True               
def checkwin(board):
    r=False
    for i in [1,4,7]:
        if board[i]==board[i+1] and board[i]==board[i+2] and board[i]!='':
            r=True
    for i in [1,2,3]:
        if board[i]==board[i+3] and board[i]==board[i+6] and board[i]!='':
            r=True
    if board[1]==board[5] and board[5]==board[9] and board[1]!='':
        r=True
    elif board[3]==board[5] and board[5]==board[7] and board[3]!='':
        r=True
    return r
main()

    



    







